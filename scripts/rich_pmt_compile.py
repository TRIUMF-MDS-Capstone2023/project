# pylint: disable-msg=C0103
"""Parse the NA62 RICH config file and returns a precomputed lookup table."""

import sys
import re
import numpy as np

COMM_RE = re.compile(r'^#')
SCPOS_RE = re.compile(r'^SCPosition_SC_(?P<ID>\d+)=(?P<VAL>.*)')
PMTPOS_RE = re.compile(r'^PMPosition_SC_(?P<ID>\d+)=(?P<VAL>.*)')
PAIR_RE = re.compile(r'\s+')


def load_config(fname):
    """Load and parse the NA62 configuration file.

       Returns a 1952 x 3 array, rows correspond to the PMT seq. ID,
       columns are (X pos. [mm], Y pos. [mm], jura = 0/saleve = 1)
    """
    # We have 1952 PMTs
    pm_position_map = np.empty((1952, 3), dtype=np.float32)
    with open(fname, 'r', encoding='utf-8') as fh:
        for line in fh:
            if m := COMM_RE.match(line):
                continue
            if m := SCPOS_RE.match(line):
                continue
            if m := PMTPOS_RE.match(line):
                if mm := PAIR_RE.split(m.group('VAL')):
                    pm_pos = [float(i) for i in mm if i != '']
                    for g, i in enumerate([0, 2, 4, 6, 8, 10, 12, 14]):
                        idx_jura = 8*int(m.group('ID')) + g
                        #  (1952 PMs + 244 SC)
                        idx_saleve = 8*int(m.group('ID')) + \
                            g + ((2196 - 244) // 2)
                        pm_position_map[idx_jura] = [pm_pos[i], pm_pos[i+1], 0]
                        pm_position_map[idx_saleve] = [
                            pm_pos[i], pm_pos[i+1], 1]

    return pm_position_map


def print_usage():
    print(
        f'usage: python {sys.argv[0]} <rich_pmt_positions.dat> <rich_pmt_positions.npy>')


def main():
    """Parse the NA62 RICH config file and returns a precomputed lookup table."""
    if len(sys.argv) != 3:
        print_usage()
        return -1
    pm_pos_map = load_config(sys.argv[1])
    np.save(sys.argv[2], pm_pos_map)
    return 0


if __name__ == '__main__':
    sys.exit(main())
