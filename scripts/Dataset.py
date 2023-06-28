import numpy as np
import polars as pl
import torch
device = 'cuda' if torch.cuda.is_available() else 'cpu'

path = '.../data'
train_file = 'point_net_[train_muons,cut_off_time=0.5,sample_size=50].parquet'

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
            )
        }

        return values