import torch
import torch.nn as nn
import torch.nn.functional as F

class TNet(nn.Module):
    def __init__(self, k = 64):
        """Initialize

        Args:
            k (int, optional): Number of features. Defaults to 64.
        """
        super(TNet, self).__init__()
        self.k = k

        # Convolutions in TNet Layer
        self.conv_network = nn.Sequential(
            nn.Conv1d(k, 64, 1),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Conv1d(64, 128, 1),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Conv1d(128, 1024, 1),
            nn.BatchNorm1d(1024),
            nn.ReLU()
        )
        # Fully connected TNet Layer
        self.fully_conn_network = nn.Sequential(
            nn.Linear(1024, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Linear(256, k * k)
        )

    def forward(self, x):
        """ Forward pass of the PointNet Transformation network

        Parameters
        ----------

        x : tensor
            Tensor containing the weight values from the previous pass
        
        """
        batch_size = x.size(0)
        x = self.conv_network(x)
        x = nn.AdaptiveMaxPool1d(1)(x)
        x = x.view(batch_size, -1)
        x = self.fully_conn_network(x)
        identity_matrix = torch.eye(self.k, device=x.device).view(1, self.k * self.k).repeat(batch_size, 1)
        matrix = x + identity_matrix
        return matrix.view(batch_size, self.k, self.k)


class PointNetRegression(nn.Module):
    def __init__(self, num_features = 3, num_output = 1024):
        """Initialize PointNet

        Parameters
        ----------

        num_features : int
            Number of dimensions of the input data 
        """
        super(PointNetRegression, self).__init__()
        self.input_tnet = TNet(k=num_features)
        self.feature_tnet = TNet(k=64)
        
        # Input transformation network
        self.input_transform = nn.Sequential(
            nn.Conv1d(num_features, 64, kernel_size=1),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Conv1d(64, 64, kernel_size=1),
            nn.BatchNorm1d(64),
            nn.ReLU()
            )

        
        # Feature transformation network
        self.feature_transform = nn.Sequential(
            nn.Conv1d(64, 64, kernel_size=1),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Conv1d(64, 128, kernel_size=1),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Conv1d(128, num_output, kernel_size=1),
            nn.BatchNorm1d(num_output),
            nn.ReLU()
        )

        self.conv1 = nn.Conv1d(num_features, 64, 1)
        self.conv2 = nn.Conv1d(64, 64, 1)
        self.conv3 = nn.Conv1d(64, 64, 1)
        self.conv4 = nn.Conv1d(64, 128, 1)
        self.conv5 = nn.Conv1d(128, num_output, 1)

        self.bn1 = nn.BatchNorm1d(64)
        self.bn2 = nn.BatchNorm1d(64)
        self.bn3 = nn.BatchNorm1d(64)
        self.bn4 = nn.BatchNorm1d(128)
        self.bn5 = nn.BatchNorm1d(num_output)
        
        # Fully connected layers for regression
        self.fc_regression = nn.Sequential(
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, num_output)
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
        input_tnet = self.input_tnet(x)
        x = torch.bmm(x.transpose(1, 2), input_tnet).transpose(1, 2)
        
        x = self.input_transform(x)
        
        # Feature transformation network
        feature_tnet = self.feature_tnet(x)
        x = torch.bmm(x.transpose(1, 2), feature_tnet).transpose(1, 2)
        x = self.feature_transform(x)
        print(f'x after feature_transform {x.size()} shape')

        # Global feature vector
        x = nn.AdaptiveMaxPool1d(1)(x)

        print(f'x after adaptive pooling x has a {x.size()} shape')

        x = x.view(batch_size, -1)

        print(f'x after view x has a {x.size()} shape')
        
        # Fully connected layers for regression

        x = self.fc_regression(x)

        print(f'Final x {x.size()}')
        
        return x