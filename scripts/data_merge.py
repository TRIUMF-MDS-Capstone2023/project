# pylint: disable-msg=C0103
"""Merge Parquet files and save as one combined Parquet file"""

import sys
import utils

import polars as pl


def merge(input_files, output_file):
    """Merge Parquet files and save as one combined Parquet file"""
    merged_df = pl.concat(
        [
            pl.scan_parquet(input_file)
            for input_file in input_files
        ],
        how='vertical',
        rechunk=False,
        parallel=True
    )
    utils.save_as_parquet(merged_df, output_file, "Combined")
    return 0


def print_usage():
    """Print script usage"""
    print(
        f'usage: python {sys.argv[0]} <input1.parquet> <input2.parquet> ... ' +
        '<output.parquet>')


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print_usage()
        sys.exit(1)

    sys.exit(merge(input_files=sys.argv[1:-1],
                   output_file=sys.argv[-1]))
