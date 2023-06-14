# pylint: disable-msg=C0103
"""Wrangle PointNet dataset"""

import sys

import polars as pl
import utils


def point_net_dataset_in_lazyframe(event_with_hit_features_path, hits_path,
                                   sample_size=50, seed=None):
    """
    Make a PointNet dataset in LazyFrame.

    Args:
        event_with_hit_features_path: Path to an event with hit features file
        hits_path: Path to a hits file
        sample_size: Sample size for each event, defaulted to 50

    Returns:
        pl.LazyFrame: Extracted data from the Parquet files
    """
    return (
        pl
        .scan_parquet(event_with_hit_features_path)
        .select(["composite_event_id", "ring_radius_cal", "class", "label", "track_momentum"])
        .filter(pl.col("ring_radius_cal").is_finite())  # filter NaNs and Nones
        .join(
            (
                pl
                .scan_parquet(hits_path)
                .select([
                    "composite_event_id",
                    "x_adjusted", "y_adjusted"
                ])
            ),
            how='inner',
            on='composite_event_id'
        )
        .groupby("composite_event_id")
        .agg([
            pl.first("ring_radius_cal"),
            pl.first("label"),
            pl.first("class"),
            pl.first("track_momentum"),
            pl.struct(["x_adjusted", "y_adjusted"])
            .sample(sample_size, with_replacement=True, seed=seed)
            .apply(lambda n: [[i["x_adjusted"], i["y_adjusted"]] for i in n])
            .alias("hits_xy_adjusted")
        ])
    )


def wrangle_point_net(event_with_hit_features_path, hits_path, sample_size,
                      output_point_net_dataset_path):
    """Wrangle PointNet dataset"""
    point_net_dataset = point_net_dataset_in_lazyframe(
        event_with_hit_features_path,
        hits_path,
        sample_size,
        seed=42
    )

    utils.save_as_parquet(point_net_dataset,
                          output_point_net_dataset_path, name="PointNet events")

    return 0


def print_usage():
    """Print script usage"""
    print(
        f'usage: python {sys.argv[0]} <event_with_hit_features_path> <hits_path> ' +
        '<sample_size> <output_point_net_dataset_path>')


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print_usage()
        sys.exit(1)

    sys.exit(wrangle_point_net(event_with_hit_features_path=sys.argv[1],
                               hits_path=sys.argv[2],
                               sample_size=int(sys.argv[3]),
                               output_point_net_dataset_path=sys.argv[4]))
