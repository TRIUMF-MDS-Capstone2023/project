import torch
import torch.nn as nn
import torch.nn.functional as F

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