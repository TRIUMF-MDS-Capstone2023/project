# pylint: disable-msg=C0103

import polars as pl
import numpy as np

from termcolor import cprint

# IDs
MUON_ID = 0
PION_ID = 1
POSITRON_ID = 2
KAON_ID = 3
BACKGROUND_ID = 4

# run_id: assumes to be max at 65536, i.e., 2 ^ 16
# burst_id: [1, 1468], 11-bit
# event_id, assumes to be max at 16777216, i.e. 2 ^ 24
# track_id: [1, 10], 4-bit
# Notice that the bit-packing sequence is different from the argument order
def compute_composite_event_id(run_id, burst_id, event_id, track_id):
    """
    Computes a composite event ID based on individual components.

    Args:
        run_id (int): Run ID.
        burst_id (int): Burst ID.
        event_id (int): Event ID.
        track_id (int): Track ID.

    Returns:
        int: Composite event ID.
    """
    return (
        (event_id & 0xffffff) |
        ((run_id & 0xffff) << 24) |
        ((burst_id & 0x7ff) << (24 + 16)) |
        ((track_id & 0xf) << (24 + 16 + 11))
    )


def decompose_composite_event_id(composite_event_id):
    """
    Decomposes a composite event ID into individual components.

    Args:
        composite_event_id (int): Composite event ID.

    Returns:
        tuple: A tuple containing the decomposed components in the following order:
               run_id (int), burst_id (int), event_id (int), track_id (int).
    """
    event_id = composite_event_id & 0xffffff
    run_id = (composite_event_id >> 24) & 0xffff
    burst_id = (composite_event_id >> (24 + 16)) & 0x7ff
    track_id = (composite_event_id >> (24 + 16 + 11)) & 0xf
    return run_id, burst_id, event_id, track_id


def get_string_label(label):
    """
    Retrieves the string label based on the given label index.

    Args:
        label (int): Label index.

    Returns:
        str: String label corresponding to the given index.
    """
    return ["muon", "pion", "positron", "kaon", "background"][label]


def get_theoretical_mass_value(label):
    """
    Retrieves the theoretical mass value based on the given label index.

    Args:
        label (int): Label index.

    Returns:
        float or None: Theoretical mass value corresponding to the given index.
    """
    return [105.66, 139.57, 0.511, 493.677, None][label]


def realign_hits(x, y, disk_id):
    """
    Realigns hit coordinates based on the disk ID.

    Args:
        x (float): X-coordinate of the hit.
        y (float): Y-coordinate of the hit.
        disk_id (int): Disk ID.

    Returns:
        tuple: A tuple containing the realigned X and Y coordinates.
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
        disk_id (int): Disk ID.
        updowndisk_id (int): Up-down disk ID.
        supercell_id (int): Supercell ID.
        or_id (int): OR ID.
        pmt_id (int): PMT ID.

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
        m (float): Mass of the particle in MeV/c^2.
        p (float): Track momentum in MeV/c.

    Returns:
        float: Expected ring radius in meters.
    """
    F_M = 17.0  # Focal length [m]
    N = 1 + 62.8e-6  # Neon refractive index
    r = (F_M * N * p
         * np.sqrt(1 - (m ** 2 + p ** 2) / (N ** 2 * p ** 2))
         / np.sqrt(m ** 2 + p ** 2))
    return r


def save_as_parquet(df, output_path, name):
    """
    Saves a DataFrame as a Parquet file and provides additional information about the DataFrame.

    Args:
        df (DataFrame): The DataFrame to be saved.
        output_path (str): The path where the Parquet file will be saved.
        name (str): The name of the DataFrame for display purposes.
    """
    cprint(f"{name} dataframe schema:", "blue")
    cprint(df.schema, "magenta")
    print()

    cprint(f"{name} dataframe samples (head):", "blue")
    cprint(df.head().collect(), "magenta")
    print()

    try:
        df.sink_parquet(output_path)
    except pl.exceptions.PolarsPanicError:
        # Not all queries support 'streaming' via `sink_parquet`.
        # Fallback if the query does not support streaming
        df.collect().write_parquet(output_path)
    cprint(f"Saved {name} dataframe as {output_path}", "green")
    print()
