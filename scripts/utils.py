# pylint: disable-msg=C0103

import polars as pl
import numpy as np

from termcolor import cprint

# IDs
MUON_ID = 0
PION_ID = 1
POSITRON_ID = 2

# event_id, assumes to be max at 16777216, i.e. 2 ^ 24
# run_id: assumes to be max at 65536, i.e., 2 ^ 16
# burst_id: [1, 1468], 11-bit
# track_id: [1, 10], 4-bit
def compute_composite_event_id(run_id, burst_id, event_id, track_id):
    return (
        (event_id) |
        (run_id << 24) |
        (burst_id << (24 + 16)) |
        (track_id << (24 + 16 + 11))
    )


def get_string_label(label):
    return ["muon", "pion", "positron"][label]


def get_theoretical_mass_value(label):
    return [105.66, 139.57, 0.511][label]


def realign_hits(x, y, disk_id):
    if disk_id == 0:
        # Jura adjustment
        return x - 146.8, y - 19.8

    # Salève alignment
    return x - 196.7, y - 9.5


def compute_pmt_seq_id(disk_id, updowndisk_id, supercell_id, or_id, pmt_id):
    """Compute the RICH PMT sequence ID"""
    if or_id < 1:
        return supercell_id * 8 + pmt_id + updowndisk_id * 61 * 8 + disk_id * 61 * 8 * 2

    return 61 * 8 * 2 * 2 + supercell_id + updowndisk_id * 61 + disk_id * 61 * 2


def calc_ring_radius(m, p):
    """
    Returns the expected ring radius [m]
    m : mass of the particle in MeV/c^2
    p : track momentum in MeV/c
    """
    F_M = 17.0  # Focal length [m]
    N = 1 + 62.8e-6  # Neon refractive index
    r = (F_M * N * p
         * np.sqrt(1 - (m ** 2 + p ** 2) / (N ** 2 * p ** 2))
         / np.sqrt(m ** 2 + p ** 2))
    return r


def save_as_parquet(df, output_path, name):
    cprint(f"{name} dataframe schema:", "blue")
    cprint(df.schema, "magenta")
    print()

    cprint(f"{name} dataframe samples (head):", "blue")
    cprint(df.head().collect(), "magenta")
    print()

    try:
        df.sink_parquet(output_path)
    except pl.exceptions.PolarsPanicError:
        # Fallback if the query does not support streaming
        df.collect().write_parquet(output_path)
    cprint(f"Saved {name} dataframe as {output_path}", "green")
    print()
