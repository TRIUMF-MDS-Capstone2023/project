# pylint: disable-msg=C0103
"""Do a uniform sampling for muon data, in the specified GeV range."""

import sys

import polars as pl

from termcolor import cprint

import utils


def uniform_sampling_muon_in_momentum(df, min_momentum, max_momentum, seed=None):
    """
    Randomly samples the same number of examples in each bin of track_momentum (bin size = 1 Gev),
    the number of examples is equal to the minimum number of examples in all the bins
    """
    bins = range(min_momentum, max_momentum + 1, 1)

    df = (
        df
        .select(['composite_event_id', 'label', 'track_momentum'])
        .filter(
            (pl.col('track_momentum') >= min_momentum) &
            (pl.col('track_momentum') <= max_momentum) &
            (pl.col('label') == utils.MUON_ID)
        )
    )
    print(
        f"Number of events within the momentum range: {df.select(pl.count()).collect()[0, 0]}")

    df = df.with_columns([
        (
            df.select('track_momentum').collect().to_series(0)
            .cut(bins)
            ["category"]
            .alias("track_momentum_bin")
        )
    ])

    min_bin_count = (
        df
        .groupby("track_momentum_bin")
        .count()
        .sort("count")
        .select(pl.min("count"))
        .collect()
        [0, 0]
    )
    print(f"Smallest bin size found: {min_bin_count}")

    return (
        df
        .with_columns([
            (
                pl.arange(0, pl.count()).shuffle(
                    seed).over("track_momentum_bin")
                .alias("rand")
            )
        ])
        .filter(pl.col("rand") < min_bin_count)
        .select("composite_event_id", "track_momentum", "track_momentum_bin")
    )


def sample(event_parquet_path, min_momentum, max_momentum, event_id_parquet_path):
    """Do a uniform sampling for muon data, in the specified GeV range."""

    # Read events
    cprint(f"Reading {event_parquet_path}", "green")
    events_df = pl.scan_parquet(event_parquet_path)

    # Sample it based on an uniform distribution
    cprint(
        f"Working on uniform sampling of muons, [{min_momentum}, {max_momentum}]", "magenta")
    sampled_composite_event_ids = (
        uniform_sampling_muon_in_momentum(
            events_df, min_momentum, max_momentum, seed=42)
        .collect()
        .to_series(0)
    )

    # And filter by the event IDs
    sampled_events_df = (
        events_df
        .filter(
            pl.col("composite_event_id")
            .is_in(sampled_composite_event_ids)
        )
    )

    print(
        f"Number of events filtered: {sampled_events_df.select(pl.count()).collect()[0, 0]}")

    # Export sampled events
    utils.save_as_parquet(
        sampled_events_df, event_id_parquet_path, name="Event")

    return 0


def print_usage():
    """Print script usage"""
    print(
        f'usage: python {sys.argv[0]} <events.parquet> <min_momentum> ' +
        '<max_momentum> <events_sampled_id.parquet>')


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print_usage()
        sys.exit(1)

    sys.exit(sample(event_parquet_path=sys.argv[1],
                    min_momentum=int(sys.argv[2]),
                    max_momentum=int(sys.argv[3]),
                    event_id_parquet_path=sys.argv[4]))
