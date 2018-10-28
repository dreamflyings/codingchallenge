#!/usr/bin/env python3

import re
import sys


def usage():
    print("Usage: " + sys.argv[0] + " file", file=sys.stderr)


if len(sys.argv) != 2:
    usage()
    sys.exit(1)

fh = open(sys.argv[1])

total = 0.0
count = 0

for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        m = re.search("(0\.[0-9]+)", line)
        if m:
            confidence = float(m.group(1))
            total += confidence
            count += 1

fh.close()

if count:
    print(total / count)
    exit(0)
else:
    exit(1)
