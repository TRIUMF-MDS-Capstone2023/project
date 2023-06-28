# pylint: disable-msg=C0103
"""Utility functions"""

import datetime

import polars as pl
import numpy as np

from termcolor import cprint

# IDs
MUON_ID = 0
PION_ID = 1
POSITRON_ID = 2
KAON_ID = 3
BACKGROUND_ID = 4


def compute_composite_event_id(run_id, burst_id, event_id, track_id):
    """
    Computes a composite event ID based on individual components.

    Args:
        run_id: Run ID.
        burst_id: Burst ID.
        event_id: Event ID.
        track_id: Track ID.

    Returns:
        int: Composite event ID.
    """
    return (
        # run_id: assumes to be max at 16777215, i.e., 2 ^ 24 - 1
        ((run_id & 0xffffff) << (4 + 24 + 11)) |
        # burst_id: [1, 1468], 11-bit
        ((burst_id & 0x7ff) << (4 + 24)) |
        # event_id, assumes to be max at 16777215, i.e. 2 ^ 24 - 1
        ((event_id & 0xffffff) << 4) |
        # track_id: [1, 10], 4-bit
        ((track_id & 0xf))
    )


def decompose_composite_event_id(composite_event_id):
    """
    Decomposes a composite event ID into individual components.

    Args:
        composite_event_id: Composite event ID.

    Returns:
        tuple: A tuple containing the decomposed components in the following order:
               `run_id`, `burst_id`, `event_id`, `track_id`.
    """
    run_id = (composite_event_id >> (4 + 24 + 11)) & 0xffffff
    burst_id = (composite_event_id >> (4 + 24)) & 0x7ff
    event_id = (composite_event_id >> 4) & 0xffffff
    track_id = (composite_event_id) & 0xf
    return run_id, burst_id, event_id, track_id


def get_string_label(label):
    """
    Retrieves the string label based on the given label index.

    Args:
        label: Label index.

    Returns:
        str: String label corresponding to the given index.
    """
    return ["muon", "pion", "positron", "kaon", "background"][label]


def get_theoretical_mass_value(label):
    """
    Retrieves the theoretical mass value based on the given label index.

    Args:
        label: Label index.

    Returns:
        float or None: Theoretical mass value corresponding to the given index.
    """
    return [105.66, 139.57, 0.51, 493.68, None][label]


def adjust_hits(x, y, disk_id):
    """
    Adjusts hit coordinates based on the disk ID.

    Args:
        x: X-coordinate of the hit.
        y: Y-coordinate of the hit.
        disk_id: Disk ID.

    Returns:
        tuple: A tuple containing the adjusted X and Y coordinates.
    """
    # disk_id == 0 : Jura
    # disk_id == 1 : Salève
    x_adjustments = [-146.8, -196.7]
    y_adjustments = [-19.8, -9.5]

    return x + x_adjustments[disk_id], y + y_adjustments[disk_id]


def compute_pmt_seq_id(disk_id, updowndisk_id, supercell_id, or_id, pmt_id):
    """
    Computes the RICH PMT sequence ID.

    Args:
        disk_id: Disk ID.
        updowndisk_id: Up-down disk ID.
        supercell_id: Supercell ID.
        or_id: OR ID.
        pmt_id: PMT ID.

    Returns:
        int: RICH PMT sequence ID.
    """
    if or_id < 1:
        return supercell_id * 8 + pmt_id + updowndisk_id * 61 * 8 + disk_id * 61 * 8 * 2

    return 61 * 8 * 2 * 2 + supercell_id + updowndisk_id * 61 + disk_id * 61 * 2


def calc_ring_radius(m, p):
    """
    Returns the expected ring radius [m] based on the given particle mass and track momentum.

    Args:
        m: Mass of the particle in MeV/c^2.
        p: Track momentum in MeV/c.

    Returns:
        float: Expected ring radius in meters.
    """
    F_M = 17.0  # Focal length [m]
    N = 1 + 62.8e-6  # Neon refractive index
    r = (F_M * N * p
         * np.sqrt(1 - (m ** 2 + p ** 2) / (N ** 2 * p ** 2))
         / np.sqrt(m ** 2 + p ** 2))
    return r


def save_as_parquet(df, output_path, name, display_head=False):
    """
    Saves a LazyFrame as a Parquet file and provides additional information about the LazyFrame.

    Args:
        df: The DataFrame to be saved.
        output_path: The path where the Parquet file will be saved.
        name: The name of the LazyFrame for display purposes.
        display_head: True if the first few rows are to be collected and shown.
    """
    cprint(f"{name} dataframe schema:", "blue")
    cprint(df.schema, "magenta")
    print()

    if display_head:
        cprint(f"{name} dataframe samples (head):", "blue")
        cprint(df.head().collect(), "magenta")
        print()

    time_start = datetime.datetime.now()
    cprint(f"Starting to persist at {time_start}", "blue")

    try:
        cprint("Trying `sink_parquet`", "blue")
        df.sink_parquet(output_path)
    except pl.exceptions.PolarsPanicError:
        # Not all queries support 'streaming' via `sink_parquet`.
        # Fallback if the query does not support streaming
        cprint("`sink_parquet` failed, fallback to `write_parquet` instead", "blue")
        df.collect().write_parquet(output_path)

    time_end = datetime.datetime.now()
    cprint(f"Saved {name} dataframe as {output_path} at {time_end}", "green")

    time_elapsed = time_end - time_start
    cprint(f"Time elapsed: {time_elapsed}", "green")
    print()
