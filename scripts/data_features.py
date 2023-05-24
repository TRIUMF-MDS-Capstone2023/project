# pylint: disable-msg=C0103
"""Derive corresponding hits as event features and save as Parquet file"""

import sys

import polars as pl
import numpy as np

from scipy.spatial.distance import pdist, squareform
from scipy.spatial import ConvexHull, QhullError

from termcolor import cprint

import utils


def hull_params(coordinates):
    """
    Compute hull parameters out of a set of coordinates.

    Args:
        coordinates: Coordinates to calculate hull parameters with.

    Returns:
        tuple: A tuple of hull width, hull diameter, absolute difference between width and
               diameter, and area. In case the hull does not fit, return `None`s.
    """
    try:
        hull = ConvexHull(coordinates)
        hull_points = hull.points[hull.vertices]

        # Area
        area = hull.area

        # Width
        widths = []
        for i, p1 in enumerate(hull_points):
            p2 = hull_points[(i+1) % len(hull_points)]
            direction = p2 - p1
            direction /= np.linalg.norm(direction)
            projections = np.dot(hull_points, direction)
            width = projections.max() - projections.min()
            widths.append(width)
        width = np.min(widths)

        # Diameter
        pairwise_dists = squareform(pdist(hull_points))
        diameter = pairwise_dists.max()

        return width, diameter, abs(width - diameter), area
    except QhullError:
        return None, None, None, None


def hit_features(hits_df, events_df):
    """
    Create a copy of LazyFrame that contains the hit features, together with all features from
    the events.

    Args:
        hits_df: A LazyFrame of the hits data.
        events_df: A LazyFrame of the events data.

    Returns:
        polars.LazyFrame: A LazyFrame of hit features
    """
    return (
        hits_df

        # Get the `track_pos_x` and `track_pos_y`
        .join(
            events_df.select("composite_event_id",
                             "track_pos_x", "track_pos_y"),
            on='composite_event_id',
            how='inner'
        )

        # With that, we "align" the hit positions, centering to the track position
        .with_columns([
            (
                (pl.col("x_adjusted") - pl.col("track_pos_x"))
                .alias("x_aligned")
            ),
            (
                (pl.col("y_adjusted") - pl.col("track_pos_y"))
                .alias("y_aligned")
            )
        ])

        # After that, we calculate the hit distances from the track position
        .with_columns([
            (
                (((pl.col("x_aligned") ** 2) + (pl.col("y_aligned") ** 2)) ** 0.5)
                .alias("hit_distance")
            )
        ])

        # Then we aggregate the following features, according to the event
        .groupby("composite_event_id")
        .agg(
            # total in time hits
            total_in_time_hits=pl.count(),

            # min/max position realigned by subtracting track position
            x_aligned_min=pl.col("x_aligned").min(),
            x_aligned_max=pl.col("x_aligned").max(),
            x_aligned_width=(
                pl.col("x_aligned").max() - pl.col("x_aligned").min()
            ),
            y_aligned_min=pl.col("y_aligned").min(),
            y_aligned_max=pl.col("y_aligned").max(),
            y_aligned_width=(
                pl.col("y_aligned").max() - pl.col("y_aligned").min()
            ),

            # hit_distance
            hit_distance_min=pl.col("hit_distance").min(),
            hit_distance_max=pl.col("hit_distance").max(),
            hit_distance_mean=pl.col("hit_distance").mean(),
            hit_distance_median=pl.col("hit_distance").median(),
            hit_distance_q25=pl.col("hit_distance").quantile(0.25),
            hit_distance_q75=pl.col("hit_distance").quantile(0.75),
            hit_distance_rms=(((pl.col("hit_distance") ** 2).mean()) ** 0.5),

            # hull-related things
            hull=(
                pl.struct("x_aligned", "y_aligned")
                .apply(lambda x: dict(zip(
                    ("hull_width", "hull_diameter",
                     "hull_diff_width_diameter", "hull_area"),
                    hull_params([list(i.values()) for i in x])
                )))
            )
        )

        # There is a bug from Polars: if we do `unnest` without `collect`,
        # it would not work, with a `PanicException` :(
        .collect()
        .unnest("hull")
        .lazy()
    )


def print_usage():
    """Print script usage"""
    print(
        f'usage: python {sys.argv[0]} <events.parquet> <hits.parquet> ' +
        '<events_with_hit_features.parquet> <cut_off_time>')


def main(event_parquet_path, hit_parquet_path,
         output_event_with_hit_features_parquet_path, cut_off_time):
    """Derive corresponding hits as event features and save as Parquet file"""

    # Read events
    cprint(f"Reading {event_parquet_path}", "green")
    events_df = pl.scan_parquet(event_parquet_path)

    # Read hits
    cprint(f"Reading {hit_parquet_path}", "green")
    hits_df = pl.scan_parquet(hit_parquet_path)

    # Limit the hits to in time hits
    hits_df = (
        hits_df
        .filter(pl.col("chod_delta") < cut_off_time)
    )

    # Engineer features and merge with the events dataframe
    events_with_hit_features = (
        hit_features(hits_df, events_df)
        .join(
            events_df,
            on='composite_event_id',
            how='inner'
        )
    )

    # And finally, save as parquet
    utils.save_as_parquet(events_with_hit_features,
                          output_event_with_hit_features_parquet_path, "Events")

    return 0


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print_usage()
        sys.exit(1)

    sys.exit(main(event_parquet_path=sys.argv[1],
                  hit_parquet_path=sys.argv[2],
                  output_event_with_hit_features_parquet_path=sys.argv[3],
                  cut_off_time=float(sys.argv[4])))
