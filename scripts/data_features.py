# pylint: disable-msg=C0103
"""Derive corresponding hits as event features and save as Parquet file"""

import sys

import circle_fit
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


def circle_fit_radii(coordinates):
    """
    Compute our own circle fit from the coordinates.

    Args:
        coordinates: Coordinates to calculate circle radius with.

    Returns:
        tuple: A tuple of fit radii. In case the coordinates do not fit, return `None`.
    """
    try:
        _x, _y, radius_fit_lsq, radius_fit_lsq_err = \
            circle_fit.standardLSQ(coordinates)
    except:
        radius_fit_lsq, radius_fit_lsq_err = None, None

    try:
        _x, _y, radius_fit_lsq_hyper, radius_fit_lsq_hyper_err = \
            circle_fit.hyperLSQ(coordinates)
    except:
        radius_fit_lsq_hyper, radius_fit_lsq_hyper_err = None, None

    try:
        _x, _y, radius_fit_riemann_swfla, radius_fit_riemann_swfla_err = \
            circle_fit.riemannSWFLa(coordinates)
    except:
        radius_fit_riemann_swfla, radius_fit_riemann_swfla_err = None, None

    try:
        _x, _y, radius_fit_svd_pratt, radius_fit_svd_pratt_err = \
            circle_fit.prattSVD(coordinates)
    except:
        radius_fit_svd_pratt, radius_fit_svd_pratt_err = None, None

    try:
        _x, _y, radius_fit_svd_taubin, radius_fit_svd_taubin_err = \
            circle_fit.taubinSVD(coordinates)
    except:
        radius_fit_svd_taubin, radius_fit_svd_taubin_err = None, None

    try:
        _x, _y, radius_fit_svd_hyper, radius_fit_svd_hyper_err = \
            circle_fit.hyperSVD(coordinates)
    except:
        radius_fit_svd_hyper, radius_fit_svd_hyper_err = None, None

    try:
        _x, _y, radius_fit_kmh, radius_fit_kmh_err = \
            circle_fit.kmh(coordinates)
    except:
        radius_fit_kmh, radius_fit_kmh_err = None, None

    return (
        radius_fit_lsq, radius_fit_lsq_err,
        radius_fit_lsq_hyper, radius_fit_lsq_hyper_err,
        radius_fit_riemann_swfla, radius_fit_riemann_swfla_err,
        radius_fit_svd_pratt, radius_fit_svd_pratt_err,
        radius_fit_svd_taubin, radius_fit_svd_taubin_err,
        radius_fit_svd_hyper, radius_fit_svd_hyper_err,
        radius_fit_kmh, radius_fit_kmh_err
    )


def hit_features(hits_df):
    """
    Create a copy of LazyFrame that contains the hit features, together with all features from
    the events.

    Args:
        hits_df: A LazyFrame of the hits data.

    Returns:
        polars.LazyFrame: A LazyFrame of hit features
    """
    return (
        hits_df

        # Aggregate the following features, according to the event
        .groupby("composite_event_id")
        .agg(
            # total in time hits
            total_in_time_hits=(
                pl.count()
                .cast(pl.UInt16)
            ),

            # min/max position realigned by subtracting track position
            x_aligned_min=(
                pl.col("x_aligned")
                .min()
                .cast(pl.Float32)
            ),
            x_aligned_max=(
                pl.col("x_aligned")
                .max()
                .cast(pl.Float32)
            ),
            x_aligned_width=(
                (pl.col("x_aligned").max() - pl.col("x_aligned").min())
                .cast(pl.Float32)
            ),
            y_aligned_min=(
                pl.col("y_aligned")
                .min()
                .cast(pl.Float32)
            ),
            y_aligned_max=(
                pl.col("y_aligned")
                .max()
                .cast(pl.Float32)
            ),
            y_aligned_width=(
                (pl.col("y_aligned").max() - pl.col("y_aligned").min())
                .cast(pl.Float32)
            ),

            # hit_distance
            hit_distance_min=(
                pl.col("hit_distance")
                .min()
                .cast(pl.Float32)
            ),
            hit_distance_max=(
                pl.col("hit_distance")
                .max()
                .cast(pl.Float32)
            ),
            hit_distance_mean=(
                pl.col("hit_distance")
                .mean()
                .cast(pl.Float32)
            ),
            hit_distance_median=(
                pl.col("hit_distance")
                .median()
                .cast(pl.Float32)
            ),
            hit_distance_q5=(
                pl.col("hit_distance")
                .quantile(0.05)
                .cast(pl.Float32)
            ),
            hit_distance_q10=(
                pl.col("hit_distance")
                .quantile(0.10)
                .cast(pl.Float32)
            ),
            hit_distance_q25=(
                pl.col("hit_distance")
                .quantile(0.25)
                .cast(pl.Float32)
            ),
            hit_distance_q75=(
                pl.col("hit_distance")
                .quantile(0.75)
                .cast(pl.Float32)
            ),
            hit_distance_q90=(
                pl.col("hit_distance")
                .quantile(0.90)
                .cast(pl.Float32)
            ),
            hit_distance_q95=(
                pl.col("hit_distance")
                .quantile(0.95)
                .cast(pl.Float32)
            ),
            hit_distance_rms=(
                (((pl.col("hit_distance") ** 2).mean()) ** 0.5)
                .cast(pl.Float32)
            ),

            # hull-related things
            hull=(
                pl.struct("x_aligned", "y_aligned")
                .apply(lambda x: dict(zip(
                    (
                        "hull_width",
                        "hull_diameter",
                        "hull_diff_width_diameter",
                        "hull_area"
                    ),
                    hull_params([list(i.values()) for i in x])
                )))
                .cast(
                    pl.Struct({
                        "hull_width": pl.Float32,
                        "hull_diameter": pl.Float32,
                        "hull_diff_width_diameter": pl.Float32,
                        "hull_area": pl.Float32
                    })
                )
            ),

            # fit-circle things
            circle_fit_radii=(
                pl.struct("x_aligned", "y_aligned")
                .apply(lambda x: dict(zip(
                    (
                        "radius_fit_lsq", "radius_fit_lsq_err",
                        "radius_fit_lsq_hyper", "radius_fit_lsq_hyper_err",
                        "radius_fit_riemann_swfla", "radius_fit_riemann_swfla_err",
                        "radius_fit_svd_pratt", "radius_fit_svd_pratt_err",
                        "radius_fit_svd_taubin", "radius_fit_svd_taubin_err",
                        "radius_fit_svd_hyper", "radius_fit_svd_hyper_err",
                        "radius_fit_kmh", "radius_fit_kmh_err"
                    ),
                    circle_fit_radii([list(i.values()) for i in x])
                )))
                .cast(
                    pl.Struct({
                        "radius_fit_lsq": pl.Float32,
                        "radius_fit_lsq_err": pl.Float32,
                        "radius_fit_lsq_hyper": pl.Float32,
                        "radius_fit_lsq_hyper_err": pl.Float32,
                        "radius_fit_riemann_swfla": pl.Float32,
                        "radius_fit_riemann_swfla_err": pl.Float32,
                        "radius_fit_svd_pratt": pl.Float32,
                        "radius_fit_svd_pratt_err": pl.Float32,
                        "radius_fit_svd_taubin": pl.Float32,
                        "radius_fit_svd_taubin_err": pl.Float32,
                        "radius_fit_svd_hyper": pl.Float32,
                        "radius_fit_svd_hyper_err": pl.Float32,
                        "radius_fit_kmh": pl.Float32,
                        "radius_fit_kmh_err": pl.Float32
                    })
                )
            )
        )

        # Break hull into separate variables
        .unnest("hull", "circle_fit_radii")
    )


def features(event_parquet_path, hit_parquet_path,
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
        .filter(pl.col("chod_delta").abs() < cut_off_time)
    )

    # Engineer features and merge with the events dataframe
    cprint(
        f"Working on engineering features with cut off time of {cut_off_time}", "magenta")

    events_with_hit_features = (
        hit_features(hits_df)
        .join(
            events_df,
            on='composite_event_id',
            how='inner'
        )
    )

    # And finally, save as parquet
    utils.save_as_parquet(events_with_hit_features,
                          output_event_with_hit_features_parquet_path, name="Events")

    return 0


def print_usage():
    """Print script usage"""
    print(
        f'usage: python {sys.argv[0]} <events.parquet> <hits.parquet> ' +
        '<events_with_hit_features.parquet> <cut_off_time>')


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print_usage()
        sys.exit(1)

    sys.exit(features(event_parquet_path=sys.argv[1],
                      hit_parquet_path=sys.argv[2],
                      output_event_with_hit_features_parquet_path=sys.argv[3],
                      cut_off_time=float(sys.argv[4])))
