#!/usr/bin/env python3

import hashlib
import os
import sys


def usage():
    print("Usage: " + sys.argv[0] + " dir", file=sys.stderr)


if len(sys.argv) != 2:
    usage()
    sys.exit(1)

dod = {}

for (dirname, subdirs, files) in os.walk(sys.argv[1]):
    for file in files:
        abspath = dirname + "/" + file

        size = os.path.getsize(abspath)

        fh = open(abspath, "rb")
        checksum = hashlib.md5(fh.read()).hexdigest()
        fh.close()

        dod[size] = dod.get(size, {})
        dod[size][checksum] = dod[size].get(checksum, [])
        dod[size][checksum].append(abspath)

for k, v in dod.items():
    size = k
    for kk, vv in dod[size].items():
        checksum = kk
        identicals = dod[size][checksum]
        if len(identicals) > 1:
            for file in identicals:
                #print(size, checksum, file)
                print(file)
            print()
