model = PointNetRegression(50, 1)
learning_rate = 0.001
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)
device = 'cuda' if torch.cuda.is_available() else 'cpu'
epochs = 25
patience = 5

import torch

def trainer(model, criterion, optimizer, trainloader, validloader, epochs = 5, patience = 5, verbose = True, device):
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

        train_loss.append(loss.item() / len(trainloader))

        # Validation Loop

        with torch.no_grad(): # Stops graph computations

            for X_valid, y_valid in enumerate(validloader):
                X_valid = d['hits'].float().to(device) # float32
                y_valid = d['ring_radius_cal'].float().to(device) # float32
                y_valid = y_valid.unsqueeze(1)
                valid_preds = model(X_valid)
                loss = criterion(valid_preds, y_valid)

                valid_batch_loss += loss.item()

            valid_loss.append(loss.item() / len(validloader))

        if verbose:
            print(f'Epoch {epoch + 1}',
                  f'Train loss: {train_loss[-1]:.3f} '
                  f'Validation loss: {valid_loss[-1]:.3f}')

        # Early stopping

        if epoch > 0 and valid_loss[-1] > valid_loss[-2]:
            consec_increases += 1
        else:
            consec_increases = 0
        if consec_increases == patience:
            print(f"Stopped early at epoch {epoch + 1} - val loss increased for {consec_increases} consecutive epochs!")
            break
    
    return train_loss, valid_loss