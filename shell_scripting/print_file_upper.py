#!/usr/bin/env python3

import sys


def usage():
    print("Usage: " + sys.argv[0] + " file", file=sys.stderr)


if len(sys.argv) != 2:
    usage()
    sys.exit(1)

fh = open(sys.argv[1])

for line in fh:
    line = line.rstrip()
    if line:
        print(line.upper())

fh.close()
