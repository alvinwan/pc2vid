"""Numpy to Javascript (JSON) conversion

Assumes numpy matrices are nx8 where first 3 columns contain x, y, z
respectively. Checks for `data/*.npy` by default, below. Uses the filename,
stripped, for the data dictionary key.

Usage:
    to_json.py
    to_json.py <start> <end>
"""


import glob
import os
import json
import numpy as np
import sys

start, end = 0, 50
arguments = sys.argv
if len(arguments) == 3:
    start, end = map(int, arguments[1:])


def convert(format):
    data = {}
    for path in list(sorted(glob.iglob(format)))[start:end]:
        key = os.path.basename(path).replace('.npy', '')
        datum = np.load(path).reshape((-1, 8)).astype(float)
        data[key] = {'vertices': [{'x': r[0], 'y': r[1], 'z': r[2]} for r in datum]}
    with open('js/output.js', 'w') as f:
        f.write('var data = %s' % json.dumps(data).replace('"', "'"))


def main():
    convert('data/*.npy')


if __name__ == '__main__':
    main()
