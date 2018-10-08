#!/usr/bin/env python3

import os
import sys

def usage():
    print("Usage: " + sys.argv[0] + " path oldext newext", file=sys.stderr)

if len(sys.argv) != 4:
    usage()
    sys.exit(1)

path = sys.argv[1]
oldext = sys.argv[2]
newext = sys.argv[3]

for root, dirs, files in os.walk(path):
    for file in files:
        oldpath = root + "/" + file
        splitext = os.path.splitext(oldpath)
        if splitext[1] == oldext:
            newpath = splitext[0] + newext
            cmd = "mv " + oldpath + " " + newpath
            #os.system(cmd)
            print("# " + cmd)

