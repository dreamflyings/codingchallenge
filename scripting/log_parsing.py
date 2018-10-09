#!/usr/bin/env python3

import heapq
import re
import sys

def usage():
    print("Usage: " + sys.argv[0] + " logfile", file=sys.stderr)

if len(sys.argv) != 2:
    usage()
    sys.exit(1)

infile = open(sys.argv[1])

tag_xacts = {}

log_pattern = re.compile("\[@(\d+)\] addr='h(\w+) data='h(\w+) tag='h(\w+)")

for line in infile:
    line = line.strip()
    if line and not line.startswith("#"):
        m = log_pattern.search(line)
        time, addr, data, tag = m.groups()

        time = int(time)
        addr = int(addr, 16)
        data = int(data, 16)
        tag = int(tag, 16)

        if not tag in tag_xacts:
            tag_xacts[tag] = []

        heapq.heappush(tag_xacts[tag], (time, (addr, data)))

for k,v in tag_xacts.items():
    tag = k
    print("tag=0x{:x}".format(tag))
    for i in range(len(v)):
        time, (addr, data) = heapq.heappop(v)
        print("[@{}] addr=0x{:x} data=0x{:x}".format(time, addr, data))

