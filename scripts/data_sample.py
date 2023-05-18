# pylint: disable-msg=C0103
"""Do a uniform sampling for muon data, in the 20-45 GeV range."""

import polars as pl

from termcolor import cprint

import utils

# TODO: Make these as CLI arguments

OUTPUT_FULL_EVENT_PARQUET = './data/full_events.parquet'
OUTPUT_FULL_HIT_PARQUET = './data/full_hits.parquet'
OUTPUT_SAMPLED_EVENT_PARQUET = './data/sampled_events.parquet'
OUTPUT_SAMPLED_HIT_PARQUET = './data/sampled_hits.parquet'


def uniform_sampling(df, min_momentum=20, max_momentum=45, seed=42):
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
    df = df.with_columns([
        (
            df.select('track_momentum').collect().to_series(0)
            .cut(bins)
            ["category"]
            .alias("momentum_bin")
        )
    ])

    min_bin_count = (
        df
        .groupby("momentum_bin")
        .count()
        .sort("count")
        .select(pl.min("count"))
        .collect()
        [0, 0]
    )
    print(f"min_bin_count: {min_bin_count}")

    return (
        df
        .with_columns([
            (
                pl.arange(0, pl.count()).shuffle(seed).over("momentum_bin")
                .alias("rand")
            )
        ])
        .filter(pl.col("rand") < min_bin_count)
        .select("composite_event_id")
        .collect()
        .to_series(0)
    )


if __name__ == "__main__":
    # Read events
    cprint(f"Reading {OUTPUT_FULL_EVENT_PARQUET}", "green")
    events_df = pl.read_parquet(OUTPUT_FULL_EVENT_PARQUET).lazy()

    # Sample it based on an uniform distribution
    sampled_composite_event_ids = uniform_sampling(events_df)

    # And get the event IDs
    sampled_events_df = events_df.filter(
        pl.col("composite_event_id").is_in(sampled_composite_event_ids))

    # Export sampled events
    utils.save_as_parquet(
        sampled_events_df, OUTPUT_SAMPLED_EVENT_PARQUET, name="Event")

    # Read hits
    cprint(f"Reading {OUTPUT_FULL_HIT_PARQUET}", "green")
    hits_df = pl.read_parquet(OUTPUT_FULL_HIT_PARQUET).lazy()

    # Extract hits from sampled event
    sampled_hits_df = hits_df.filter(
        pl.col("composite_event_id").is_in(sampled_composite_event_ids))

    # Export sampled hits
    utils.save_as_parquet(
        sampled_hits_df, OUTPUT_SAMPLED_HIT_PARQUET, name="Hit")
