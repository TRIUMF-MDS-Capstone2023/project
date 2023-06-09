import torch
from torch.utils.data import Dataset
import polars as pl


class CalorichPointNetDataset(Dataset):
    def __init__(self, point_net_dataset_path):
        """Constructor"""
        self.point_net_dataset = (
            pl.read_parquet(point_net_dataset_path)
        )

    def __len__(self):
        """Size of the dataset"""
        return self.point_net_dataset.shape[0]

    def __getitem__(self, idx):
        """Get a particular item of the dataset"""
        _, ring_radius_cal, hits_xy_adjusted = self.point_net_dataset.row(idx)
        return {
            'ring_radius_cal': torch.tensor(ring_radius_cal),
            'hits_xy_adjusted': torch.tensor(hits_xy_adjusted)
        }
