#!/usr/bin/env python3

import re
import sys


def usage():
    print("Usage: " + sys.argv[0] + " file", file=sys.stderr)


if len(sys.argv) != 2:
    usage()
    sys.exit(1)

count = 0
total = 0

fh = open(sys.argv[1])  # mbox-simple.txt

for line in fh:
    line = line.rstrip()
    r = re.findall("^New Revision: (\d+)", line)
    if r:
        total += int(r[0])
        count += 1

fh.close()

print(total / count)
