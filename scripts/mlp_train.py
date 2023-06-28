"""
Multi-layer Perceptron (MLP) regression implementation for the CaloRICH AI MDS Capstone project (2023).

"""

import numpy as np
import pandas as pd
import torch
from torch import nn
import pyarrow as pa
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, TensorDataset, random_split
import torch.optim as optim

# below code can be modified based on device availability
device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')

# Read in parquet files and drop NAs
event_with_hit_features_path = '../data/events_with_hit_features_[cut_off_time=0.5].parquet'
df = pd.read_parquet(event_with_hit_features_path).dropna()

# filter df for muons only
df_muons = df.query('label==0')

# split for train and test dataset
train_df, test_df_muon = train_test_split(df_muons,
                                          random_state=42)

# add pions data into test dataset
test_df = pd.concat([test_df_muon, df.query('label==1')])

# select engineered features for model training
input_features = ['total_in_time_hits','x_aligned_min','x_aligned_max','x_aligned_width',
                  'y_aligned_min','y_aligned_max','y_aligned_width','hit_distance_min',
                  'hit_distance_max','hit_distance_mean','hit_distance_median',
                  'hit_distance_q25','hit_distance_q75','hit_distance_rms',
                  'hull_area','hull_diameter','hull_diff_width_diameter','hull_width']

X_train_raw, y_train = train_df[input_features], train_df['ring_radius_cal']
X_test_raw, y_test = test_df[input_features], test_df['ring_radius_cal']

# Standardizing data
scaler = StandardScaler()
scaler.fit(X_train_raw)
X_train = scaler.transform(X_train_raw)
X_test = scaler.transform(X_test_raw)

# convert data to tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train.to_numpy().flatten(), dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test.to_numpy().flatten(), dtype=torch.float32)

# split trainset to train and validation
trainset = TensorDataset(X_train, y_train)
train_size = int(0.6 * len(trainset)) # 60% of train data
val_size = len(trainset) - train_size
generator1 = torch.Generator().manual_seed(42)
train_set, val_set = random_split(dataset=trainset,
                                  lengths=[train_size, val_size],
                                  generator=generator1)

# create dataloader
BATCH_SIZE = 1000 # adjust batch size based on computation resources
trainloader = DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True)
validloader = DataLoader(val_set, batch_size=BATCH_SIZE, shuffle=True)

# define mlp model
def linear_block(input_size, output_size):
    """
    A linear transformation block.

    Parameters
    ----------
    input_size : int
        the input size of the layer
    output_size : int
        the output size of the layer

    Returns
    -------
    torch.nn.Sequential
        a sequential container calling a sequence of modules

    Examples
    --------
    >>> linear_block(12, 1)
    """
    return nn.Sequential(
        nn.Linear(input_size, output_size),
        nn.ReLU()
    )

class MLPregression(nn.Module):
    """MLP regression implementation in PyTorch."""
    def __init__(self, input_size):
        super().__init__()
        self.main = nn.Sequential(
            linear_block(input_size, 1024),
            linear_block(1024, 512),
            linear_block(512, 256),
            linear_block(256, 64),
            linear_block(64, 12),
            nn.Linear(12, 1)
        )

    def forward(self, x):
        out = self.main(x)
        return out

# make an instance of mlp
model = MLPregression(len(input_features))
model.to(device)

# define a trainer
# below code adopted from MDS DSCI 572 Lecture 5 notes
def trainer(model, criterion, optimizer, trainloader, validloader, epochs=5, patience=5, verbose=True):
    """
    A training wrapper for PyTorch network.

    Parameters
    ----------
    model : model class
        defined model class inheriting from nn.Module
    criterion : torch.nn.modules.loss
        a loss function in PyTorch
    optimizer : optimizer class
        an optimization algorithm
    trainloader : torch.utils.data.DataLoader
        a dataloader for training data   
    validloader : torch.utils.data.DataLoader
        a dataloader for validation data          
    epochs : int, default is 5
        one full pass through the dataset to look at all observations         
    patience : int, default is 5
        a number of consecutive epochs to allow the validation loss to increase before stopping   
    verbose : bool, default is True
        whether or not to print additional details when running the function         

    Returns
    -------
    float
        train_loss, valid_loss
    """

    train_loss = []
    valid_loss = []

    for epoch in range(epochs):
        train_batch_loss = 0
        valid_batch_loss = 0

        # Training
        for X, y in trainloader:
            X, y = X.to(device), y.to(device)
            optimizer.zero_grad()       # Clear gradients w.r.t. parameters
            y_hat = model(X).flatten()  # Forward pass to get output
            loss = criterion(y_hat, y)  # Calculate loss
            loss.backward()             # Getting gradients w.r.t. parameters
            optimizer.step()            # Update parameters
            train_batch_loss += loss.item()       # Add loss for this batch to running total

        train_loss.append(train_batch_loss / len(trainloader))

        # Validation
        with torch.no_grad():  # this stops pytorch doing computational graph stuff under-the-hood

            for X_valid, y_valid in validloader:
                X_valid, y_valid = X_valid.to(device), y_valid.to(device)
                y_hat = model(X_valid).flatten()  # Forward pass to get output
                loss = criterion(y_hat, y_valid)  # Calculate loss based on output

                valid_batch_loss += loss.item()

        valid_loss.append(valid_batch_loss / len(validloader))

        # Print progress
        if verbose:
            print(f"Epoch {epoch + 1:3}:",
                  f"Train Loss: {train_loss[-1]:.3f}.",
                  f"Valid Loss: {valid_loss[-1]:.3f}.")

        # Early stopping
        if epoch > 0 and valid_loss[-1] > valid_loss[-2]:
            consec_increases += 1
        else:
            consec_increases = 0
        if consec_increases == patience:
            print(f"Stopped early at epoch {epoch + 1} - val loss increased for {consec_increases} consecutive epochs!")
            break

    return train_loss, valid_loss

# model training
LEARNING_RATE = 0.0001
criterion = nn.MSELoss() # loss function
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)
train_loss, valid_loss = trainer(model,
                                 criterion,
                                 optimizer,
                                 trainloader,
                                 validloader,
                                 epochs=30,
                                 patience=5,
                                 verbose=True)

# Save the trained model
torch.save(model.state_dict(), '../saved_models/mlp_model.pth')