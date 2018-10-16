#!/usr/bin/env python3

import sys

def usage():
    print("Usage: " + sys.argv[0] + " file", file=sys.stderr)

if len(sys.argv) != 2:
    usage()
    sys.exit(1)

file = open(sys.argv[1])

first_row = []
rows = []

for line in file:
   line = line.rstrip()
   if line:
     row = line.split(" ")
     if not first_row:
       first_row = row
     else:
       rows.append(row)

file.close()

# first_row = [name, age]
# rows = [[alice, 21], [ryan, 30], [patrick, 13]]]

lines = ["" for _ in range(len(first_row))]

for i in range(len(first_row)): # [0, 1]
    lines[i] += first_row[i] + " "
    for j in range(len(rows)): # [0,2]
        lines[i] += rows[j][i] + " "

for line in lines:
    print(line)

