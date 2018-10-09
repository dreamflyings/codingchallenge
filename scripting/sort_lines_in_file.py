#!/usr/bin/env python3

import sys

def usage():
    print("Usage: " + sys.argv[0] + " file", file=sys.stderr)

if len(sys.argv) != 2:
    usage()
    sys.exit(1)

lines = [line.rstrip() for line in open(sys.argv[1])]

for line in sorted(lines):
    print(line)

