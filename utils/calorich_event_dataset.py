import torch
from torch.utils.data import Dataset
import polars as pl


class CalorichEventDataset(Dataset):
    """
    Class that creates a dataset object for use in a dataloader function

    Args:
        Dataset: Filepath to the parquet file that contains the hits data to be used in the DNN
    """
    def __init__(self, event_with_hit_features_path, hits_path):
        """Constructor"""
        self.event_with_hit_features_columns = [
            'composite_event_id',  # Remember to drop
            'total_in_time_hits',
            'x_aligned_min', 'x_aligned_max', 'x_aligned_width',
            'y_aligned_min', 'y_aligned_max', 'y_aligned_width',
            'hit_distance_min', 'hit_distance_max', 'hit_distance_mean', 'hit_distance_median',
            'hit_distance_q25', 'hit_distance_q75', 'hit_distance_rms',
            'hull_area', 'hull_diameter', 'hull_diff_width_diameter', 'hull_width',
            'track_momentum', 'chod_time',
            'track_pos_x', 'track_pos_y',
            'total_hits', 'ring_radius_cal'
        ]

        self.event_with_hit_features = (
            pl
            .read_parquet(event_with_hit_features_path)
            .select(self.event_with_hit_features_columns)
            .drop_nulls()
        )

        self.hits_columns = [
            'composite_event_id',  # Remember to drop
            'x_adjusted', 'y_adjusted', 'chod_delta'
        ]

        self.hits = (
            pl
            .scan_parquet(hits_path)
            .select(self.hits_columns)
        )

    def __len__(self):
        """Size of the dataset"""
        return self.event_with_hit_features.shape[0]

    def __getitem__(self, idx):
        """Get a particular item of the dataset and output a dictionary containing the hits as a 
        n*3 tensor array"""
        row = self.event_with_hit_features.row(idx)

        composite_event_id = row[0]

        hits = (
            self.hits
            .filter(pl.col("composite_event_id") == composite_event_id)
            .drop("composite_event_id")
            .collect()
        )

        # [1:] to remove the ID when training
        return dict(zip(
            self.event_with_hit_features_columns[1:],
            torch.tensor(
                [n for n in self.event_with_hit_features.row(idx)[1:]])
        )) | {
            # Hits is now a n*3 tensor array
            "hits": torch.tensor(hits.rows())
        }
