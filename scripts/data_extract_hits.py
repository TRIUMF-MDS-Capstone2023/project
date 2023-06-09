# pylint: disable-msg=C0103
"""Extract the hits and save as Parquet files"""

import sys

import h5py
import polars as pl
import numpy as np

from termcolor import cprint

import utils


def event_hitmapping_to_lazyframe(f):
    """
    Extract all event mappings from the H5 source file and put it in `pl.LazyFrame`.

    Args:
        f: An h5py.File

    Returns:
        pl.LazyFrame: Extracted event mappings from the source file
    """
    events = f["Events"]

    # First, create an event dataframe, and calculate the composite event ID
    # used for mapping
    composite_event_ids = (
        pl.LazyFrame({
            "run_id": events["run_id"],
            "burst_id": events["burst_id"],
            "event_id": events["event_id"],
            "track_id": events["track_id"]
        })
        .with_columns([
            (
                pl.col("run_id")
                .cast(pl.UInt32)
            ),
            (
                pl.col("burst_id")
                .cast(pl.UInt16)
            ),
            (
                pl.col("event_id")
                .cast(pl.UInt64)
            ),
            (
                pl.col("track_id")
                .cast(pl.UInt8)
            ),
            (
                pl.struct(["run_id", "burst_id", "event_id", "track_id"])
                .apply(lambda x: (
                    utils.compute_composite_event_id(
                        x["run_id"], x["burst_id"], x["event_id"], x["track_id"]
                    )
                ))
                .cast(pl.UInt64)
                .alias("composite_event_id")
            )
        ])
        .select("composite_event_id")
        .collect()
        .to_series(0)
    )

    # Make a linear mapping, so that it is faster, though a bit more memory-
    # intensive, to be used in a join
    return (
        pl.LazyFrame({
            "hit_id": range(f['Hits'].size)
        })
        .join(
            pl.LazyFrame({
                "hit_id": np.array(f['HitMapping'])[:-1],
                "composite_event_id": composite_event_ids
            }),
            how='left',
            on='hit_id'
        )
        .select(pl.all().forward_fill())
        .sort("hit_id")
    )


def hits_to_lazyframe(f, position_map):
    """
    Extract all hits from the H5 source file and put it in `pl.LazyFrame`.

    Args:
        f: An h5py.File
        position_map: A `pl.LazyFrame` of position map

    Returns:
        pl.LazyFrame: Extracted hits from the source file
    """
    hits = f["Hits"]

    return (
        pl.LazyFrame({
            "hit_id": range(hits.shape[0]),
            "assigned_flag": hits["assigned_flag"],
            "disk_id": hits["disk_id"],
            "pmt_id": hits["pmt_id"],
            "supercell_id": hits["supercell_id"],
            "updowndisk_id": hits["updowndisk_id"],
            "hit_time": hits["hit_time"]
        })
        .with_columns([
            (
                pl.col("assigned_flag")
                .cast(pl.Int32)
            ),
            (
                pl.col("disk_id")
                .cast(pl.UInt8)
            ),
            (
                pl.col("pmt_id")
                .cast(pl.UInt8)
            ),
            (
                pl.col("supercell_id")
                .cast(pl.UInt8)
            ),
            (
                pl.col("updowndisk_id")
                .cast(pl.UInt8)
            ),
            (
                # Algorithm modified from `compute_pmt_seq_id`
                # In this slice, `or_id` is always 0
                (
                    pl.col("pmt_id") +
                    pl.col("supercell_id") * 8 +
                    pl.col("updowndisk_id") * 61 * 8 +
                    pl.col("disk_id") * 61 * 8 * 2
                )
                .cast(pl.UInt32)
                .alias("pmt_idx")
            )
        ])
        .join(
            position_map,
            on="pmt_idx"
        )
        .with_columns([
            pl.col("x").alias("x_raw"),
            pl.col("y").alias("y_raw"),
            # Algorithm modified from `adjust_hits`
            (
                pl.when(pl.col("disk_id") == 0)
                .then(pl.col("x") - 146.8)
                .otherwise(pl.col("x") - 196.7)
                .cast(pl.Float32)
                .alias("x_adjusted")
            ),
            (
                pl.when(pl.col("disk_id") == 0)
                .then(pl.col("y") - 19.8)
                .otherwise(pl.col("y") - 9.5)
                .cast(pl.Float32)
                .alias("y_adjusted")
            )
        ])
        # Drop to minimize confusion
        # {x,y}_raw: The raw number at sensor
        # {x,y}_adjusted: The adjusted number, by `disk_id`
        .drop(["x", "y"])
    )


def position_map_to_lazyframe(position_map_path):
    """
    Extract all event mappings from a Numpy file and put it in `pl.LazyFrame`.

    Args:
        position_map_path: A path to the position map

    Returns:
        pl.LazyFrame: Extracted event mappings from the source file
    """
    position_map = pl.from_numpy(
        np.load(position_map_path), schema=["x", "y", "disk_id"])
    position_map = position_map.insert_at_idx(
        0,
        pl.Series(
            "pmt_idx",
            range(position_map.shape[0]),
            dtype=pl.UInt32
        )
    )
    position_map = position_map.drop("disk_id")
    return position_map.lazy()


def extract_hits(dataset_path, event_parquet_path, position_map_path, hit_parquet_path):
    """Extract the hits and save as Parquet files"""

    # Read H5 dataset
    cprint(f"Reading {dataset_path}", "green")

    with h5py.File(dataset_path, 'r') as raw_file:
        # Read events
        cprint(f"Reading {event_parquet_path}", "green")
        events_df = pl.scan_parquet(event_parquet_path)

        # Read position map
        cprint(f"Reading {position_map_path}", "green")
        position_map = position_map_to_lazyframe(position_map_path)

        # Work on hits
        cprint("Working on hits", "magenta")

        # First, retrieve an event-to-hit mapping
        event_hit_mapping = event_hitmapping_to_lazyframe(raw_file)

        # Then, retrieve the hits, and
        hits_df = (
            hits_to_lazyframe(raw_file, position_map)

            # Use the event_id from the mapping
            .join(
                event_hit_mapping,
                how='inner',
                on='hit_id'
            )

            # Merge with events for some additional columns
            .join(
                (
                    events_df
                    .select(["composite_event_id",
                             "run_id", "burst_id", "event_id", "track_id",
                             "track_pos_x", "track_pos_y",
                             "chod_time", "class", "track_momentum"])
                ),
                how='inner',
                on='composite_event_id'
            )

            # Then calculate the `chod_delta`, and also "align" the hit positions, centering to the
            # track position
            .with_columns([
                (
                    (pl.col("hit_time") - pl.col("chod_time"))
                    .cast(pl.Float32)
                    .alias("chod_delta")
                ),
                (
                    (pl.col("x_adjusted") - pl.col("track_pos_x"))
                    .cast(pl.Float32)
                    .alias("x_aligned")
                ),
                (
                    (pl.col("y_adjusted") - pl.col("track_pos_y"))
                    .cast(pl.Float32)
                    .alias("y_aligned")
                )
            ])

            # Since we are there, why not we calculate the hit distances from the track position
            # as well. (Technically it is more like a feature engineering step, but doing it a
            # step earlier will be faster for latter processing.)
            .with_columns([
                (
                    (((pl.col("x_aligned") ** 2) + (pl.col("y_aligned") ** 2)) ** 0.5)
                    .cast(pl.Float32)
                    .alias("hit_distance")
                )
            ])
        )

        # Export hits
        utils.save_as_parquet(hits_df, hit_parquet_path, name="Hit")

    return 0


def print_usage():
    """Print script usage"""
    print(
        f'usage: python {sys.argv[0]} <dataset_path> <position_map_path> ' +
        '<events.parquet> <hits.parquet>')


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print_usage()
        sys.exit(1)

    sys.exit(extract_hits(dataset_path=sys.argv[1],
                          event_parquet_path=sys.argv[2],
                          position_map_path=sys.argv[3],
                          hit_parquet_path=sys.argv[4]))
