# pylint: disable-msg=C0103
"""Extract the events and save as Parquet files"""

import sys

import h5py
import polars as pl
import numpy as np

from termcolor import cprint

import utils


def events_to_lazyframe(f):
    """
    Extract all events from the H5 source file and put it in `pl.LazyFrame`.

    Args:
        f: An h5py.File

    Returns:
        pl.LazyFrame: Extracted events from the source file
    """
    events = f["Events"]
    hit_mapping = np.array(f["HitMapping"])

    # Labels
    mu_off = f.attrs["muon_offset"]
    pi_off = f.attrs["pion_offset"]
    pos_off = f.attrs["positron_offset"]
    entries = f.attrs["entries"]

    labels = np.zeros(entries, dtype=np.int32)
    labels[mu_off:pi_off] = utils.MUON_ID
    labels[pi_off:pos_off] = utils.PION_ID
    labels[pos_off:] = utils.POSITRON_ID

    return (
        pl.LazyFrame({
            "run_id": events["run_id"],
            "burst_id": events["burst_id"],
            "event_id": events["event_id"],
            "track_id": events["track_id"],
            "track_momentum": events["track_momentum"],
            "chod_time": events["chod_time"],
            "track_pos_x": events["track_pos"][:, 0],
            "track_pos_y": events["track_pos"][:, 1],
            "ring_radius": events["ring_radius"],
            "ring_centre_pos_x": events["ring_centre_pos"][:, 0],
            "ring_centre_pos_y": events["ring_centre_pos"][:, 1],
            "ring_likelihood_pion": events["ring_likelihood"][:, 0],
            "ring_likelihood_muon": events["ring_likelihood"][:, 1],
            "ring_likelihood_positron": events["ring_likelihood"][:, 2],
            "ring_likelihood_kaon": events["ring_likelihood"][:, 3],
            "ring_likelihood_background": events["ring_likelihood"][:, 4],
            "label": labels,
            "first_hit": hit_mapping[:-1],  # hit n
            "last_hit": hit_mapping[1:]    # hit n+1
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
                pl.col("label")
                .cast(pl.UInt8)
            ),
            (
                pl.col("first_hit")
                .cast(pl.UInt64)
            ),
            (
                pl.col("last_hit")
                .cast(pl.UInt64)
            ),
            (
                (pl.col("last_hit") - pl.col("first_hit"))
                .cast(pl.UInt16)
                .alias("total_hits")
            )
        ])
        .drop(["first_hit", "last_hit"])
    )


def extract_events(dataset_path, event_parquet_path):
    """Extract the events and save as Parquet files"""

    # Read H5 dataset
    cprint(f"Reading {dataset_path}", "green")

    with h5py.File(dataset_path, 'r') as raw_file:
        # Work on events
        cprint("Working on events", "magenta")
        events_df = (
            events_to_lazyframe(raw_file)

            # Ignore positron, kaon, and background entries
            .filter(
                pl.col("label").is_in([utils.MUON_ID, utils.PION_ID])
            )

            # Add in additional columns, including...
            .with_columns([
                # class label
                (
                    pl.col("label")
                    .apply(utils.get_string_label)
                    # Not sure why, but Categorical type cannot be properly read...
                    .cast(pl.Utf8)
                    .alias("class")
                ),
                # theoretical mass value (MeV)
                (
                    pl.col("label")
                    .apply(utils.get_theoretical_mass_value)
                    .cast(pl.Float32)
                    .alias("mass")
                ),
                # and `composite_event_id`, for an event is only unique
                # when we consider all of the columns
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

            # Then add the calculated ring radius
            .with_columns([
                (
                    pl.struct(['mass', 'track_momentum'])
                    .apply(lambda x: (
                        utils.calc_ring_radius(
                            x['mass'], x['track_momentum'] * 1000) * 1000
                    ))
                    .cast(pl.Float32)
                    .alias("ring_radius_cal")
                )
            ])
        )

        # Export events
        utils.save_as_parquet(events_df, event_parquet_path, name="Event")

    return 0


def print_usage():
    """Print script usage"""
    print(
        f'usage: python {sys.argv[0]} <dataset_path> <events.parquet>')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)

    sys.exit(extract_events(dataset_path=sys.argv[1],
                            event_parquet_path=sys.argv[2]))
