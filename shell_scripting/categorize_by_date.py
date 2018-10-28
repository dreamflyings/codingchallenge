#!/usr/bin/env python3

import sys


def usage():
    print("Usage: " + sys.argv[0] + " file", file=sys.stderr)


if len(sys.argv) != 2:
    usage()
    sys.exit(1)

fh = open(sys.argv[1])

counts = {}

for line in fh:
    line = line.rstrip()
    if line.startswith("From"):
        tokens = line.split(" ")
        if len(tokens) > 2:
            day = tokens[2]
            counts[day] = counts.get(day, 0)
            counts[day] += 1

for day, count in counts.items():
    print(day, count)

fh.close()
