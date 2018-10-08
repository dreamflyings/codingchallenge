#!/usr/bin/env python3

import sys

def usage():
    print("Usage: " + sys.argv[0] + " infile", file=sys.stderr)

if len(sys.argv) != 2:
    usage()
    sys.exit(1)

infile = open(sys.argv[1])

for line in infile:
    print(line.replace('\t',',').rstrip())

