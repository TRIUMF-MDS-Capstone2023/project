"""
PointNet DNN model
"""

import pyarrow.parquet as pq
import pandas as pd
import numpy as np
import torch
device = 'cuda' if torch.cuda.is_available() else 'cpu'
import time
torch.backends.cudnn.benchmark = True
import os
import polars as pl
from torch.utils.data import Dataset
import platform
import seaborn as sbn
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader
from torch.utils.data.sampler import SubsetRandomSampler
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


# Create dataset

class CalorichPointNetDataset(Dataset):
    def __init__(self, point_net_dataset_path):
        """Constructor
        
        Parameters
        ----------
        
        point_net_dataset_path : str
            Path to the location of the parquet containing the RICH preprocessed data
        """
        
        self.point_net_dataset = (
            pl.read_parquet(point_net_dataset_path)
            .filter(pl.col('ring_radius_cal').is_not_nan())
        )

    def __len__(self):
        """Size of the dataset"""
        return self.point_net_dataset.shape[0]

    def __getitem__(self, idx):
        """Get a particular item of the dataset
        
        Parameters
        ----------

        idx : int
            The index number for the desired item

        Returns
        -------

        Dict : Dictionary containing a tensor with the calculated ring radius (ring_radius_cal)
        and the hits assigned to the event in a 3 dimensional tensor each
        """
        
        # Add random noise to generate a 3rd dimension
        noise = np.random.normal(0, 0.05, 50)
        noise = np.expand_dims(noise, 1)
        noise = torch.Tensor(noise)
        
        values = {
            "hits": (
                torch.cat((torch.tensor(self.point_net_dataset.select("hits_xy_adjusted").row(idx)).squeeze(), noise), -1).to(device)
            ),
            "ring_radius_cal":(
                torch.tensor(self.point_net_dataset.select("ring_radius_cal").row(idx)).squeeze().to(device)
            ),
            "composite_id":(
                torch.tensor(self.point_net_dataset.select("composite_event_id").row(idx)).squeeze().to(device)
            )
        }

        return values


        return values
    
path = 'data'
file_name = 'point_net_[cut_off_time=0.5,sample_size=50].parquet'

dataset = CalorichPointNetDataset(os.path.join(path, file_name))

train_dataset, test_dataset = train_test_split(dataset, test_size= 0.2, random_state= 42, shuffle= True)


# Create train_loader and validation_loader dataloaders

batch_size = 1024
validation_split = 0.2
shuffle_dataset = True
random_seed = 42
num_workers = 0
pin_memory = False
dataset_used = train_dataset

indices = list(range(dataset_used.__len__()))
split = int(np.floor(validation_split * dataset_used.__len__()))
if shuffle_dataset :
    np.random.seed(random_seed)
    np.random.shuffle(indices)
train_indices, val_indices = indices[split:], indices[:split]

train_sampler = SubsetRandomSampler(train_indices)
valid_sampler = SubsetRandomSampler(val_indices)

train_loader = DataLoader(dataset_used, batch_size=batch_size, 
                                           sampler=train_sampler, num_workers = num_workers, pin_memory = pin_memory)
validation_loader = DataLoader(dataset_used, batch_size=batch_size,
                                                sampler=valid_sampler, num_workers = num_workers, pin_memory = pin_memory)

# PointNet_1 architecture (simple)

class PointNetRegression(nn.Module):
    def __init__(self, num_features, num_output):
        """Initialize PointNet

        Parameters
        ----------

        num_features : int
            Number of dimensions of the input data 
        """
        
        super(PointNetRegression, self).__init__()
        
        # Input transformation network
        self.input_transform = nn.Sequential(
            nn.Conv1d(num_features, 64, kernel_size=1),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Conv1d(64, 128, kernel_size=1),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Conv1d(128, 1024, kernel_size=1),
            nn.BatchNorm1d(1024),
            nn.ReLU()
        )
        
        # Feature transformation network
        self.feature_transform = nn.Sequential(
            nn.Conv1d(1024, 512, kernel_size=1),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Conv1d(512, 256, kernel_size=1),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Conv1d(256, 128, kernel_size=1),
            nn.BatchNorm1d(128),
            nn.ReLU()
        )
        
        # Fully connected layers for regression
        self.fc_regression = nn.Sequential(
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, num_output)
        )

    def forward(self, x):
        """ Forward pass of the PointNet network

        Parameters
        ----------

        x : tensor
            Tensor containing the weight values from the previous pass
        
        """

        batch_size = x.size(0)
        
        # Input transformation network
        x = self.input_transform(x)
        
        # Global feature extraction
        x = torch.max(x, 2, keepdim=True)[0]
        
        # Feature transformation network
        x = self.feature_transform(x)
        
        # Global feature vector
        x = torch.max(x, 2, keepdim=False)[0]

        # Fully connected layers for regression
        x = self.fc_regression(x)
        
        return x

# Trainer

def trainer(model, criterion, optimizer, trainloader, validloader, epochs = 5, patience = 5, verbose = True):
    """
Training loop for the PointNet architecture

    Args:
        model (class): Model architecture class to be trained
        criterion (function): The loss function from pyTorch to be used
        optimizer (function): The optimizer function from pyTorch to be used
        trainloader (loader): Loader with the training data
        validloader (loader): Loader with the validation data
        device (string): Name of the device to be used while training (CUDA or CPU)
        epochs (int, optional): Number of epochs in the training loop. Defaults to 5.
        patience (int, optional): Number of consecutive epochs without a decrease in validation loss before stopping the training. Defaults to 5.
        verbose (bool, optional): If True displays the training and validation loss values along with the latest calculated epoch. Defaults to True.

    Returns:
        array: Returns 2 arrays, one containing the train losses per epoch and one containing the validation loss per epoch
    """    
    

    train_loss = []
    valid_loss = []
    model.to(device)

    for epoch in range(epochs):

        train_batch_loss = 0
        valid_batch_loss = 0

        # Start the trainer

        for i, d in enumerate(trainloader):
            X = d['hits'].float().to(device)
            y = d['ring_radius_cal'].float().to(device)
            y = y.unsqueeze(1)

            # Model is used
            optimizer.zero_grad()
            predictions = model(X)

            # Loss
        
            loss = criterion(predictions, y)
            loss.backward()
            optimizer.step()
            train_batch_loss += loss.item()

        train_loss.append(loss.item() / len(train_loader))

        # Validation Loop

        with torch.no_grad(): # Stops graph computations

            for X_valid, y_valid in enumerate(validloader):
                X_valid = d['hits'].float().to(device) # float32
                y_valid = d['ring_radius_cal'].float().to(device) # float32
                y_valid = y_valid.unsqueeze(1)
                valid_preds = model(X_valid)
                loss = criterion(valid_preds, y_valid)

                valid_batch_loss += loss.item()

            valid_loss.append(loss.item() / len(validation_loader))

        if verbose:
            print(f'Epoch {epoch + 1}',
                  f'Train loss: {train_loss[-1]:.3f} '
                  f'Validation loss: {valid_loss[-1]:.3f}')
            
        if epoch > 0 and valid_loss[-1] > valid_loss[-2]:
            consec_increases += 1
        else:
            consec_increases = 0
        if consec_increases == patience:
            print(f"Stopped early at epoch {epoch + 1} - val loss increased for {consec_increases} consecutive epochs!")
            break
    
    return train_loss, valid_loss

# Training loop

model = PointNetRegression(50, 1)
learning_rate = 0.001
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)
device = 'cuda' if torch.cuda.is_available() else 'cpu'
epochs = 25
patience = 5

train_loss, valid_loss = trainer(model, 
                                 criterion, 
                                 optimizer, 
                                 train_loader,
                                 validation_loader,
                                 epochs=epochs, 
                                 patience=patience,
                                 verbose=True)

# Save results

torch.save(model.state_dict(), 'saved_models/pointnet_1_states.pth')

# Testing

model = PointNetRegression(50, 1)
model.load_state_dict(torch.load('saved_models/pointnet_1_states.pth', map_location = device))
model.eval()

test_loader = DataLoader(test_dataset, batch_size=4000, num_workers = 0, pin_memory = False)

# Get predictions

results = []
calc_ring_radius = []
composite_id = []

with torch.no_grad():
            for i, d in enumerate(test_loader):
                X = d['hits'].float()
                y = d['ring_radius_cal'].float().to(device)
                y = y.unsqueeze(1)
                comp_id = d['composite_id'].to(device)

                preds = model(X)
                preds_arr = preds.detach().cpu().numpy()

                results.append(preds_arr)
                y_arr = y.detach().cpu().numpy()
                calc_ring_radius.append(y_arr)

                id_arr = comp_id.detach().cpu().numpy()
                composite_id.append(id_arr)

# Create results dataframe

composite_events_id = []
for i in np.arange(0, len(composite_id)):
    for j in composite_id[i]:
        composite_events_id.append(j)

entire_results = np.vstack(results)
entire_calc_ring = np.vstack(calc_ring_radius)

residuals = np.subtract(entire_calc_ring, entire_results)

residuals_df = pd.DataFrame(list(zip(entire_results.ravel().tolist(), entire_calc_ring.ravel().tolist(), residuals.ravel().tolist(), composite_events_id)),
columns = ['Predicted', 'Theoretical', 'Residuals', 'composite_events_id'])

residuals_df = pl.from_pandas(residuals_df)

residuals_df.write_csv('saved_models/pointnet_1_results.csv') #Output predictions and residuals dataframe that can be used for analysis