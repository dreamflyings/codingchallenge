#!/usr/bin/env python3

import sys


def usage():
    print("Usage: " + sys.argv[0] + " file", file=sys.stderr)


if len(sys.argv) != 2:
    usage()
    sys.exit(1)

count = 0

fh = open(sys.argv[1])  # mbox-short.txt

for line in fh:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line.split(" ")[1])
        count += 1

fh.close()

print(count)
