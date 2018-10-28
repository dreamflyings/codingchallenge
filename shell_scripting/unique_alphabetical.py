#!/usr/bin/env python3

import sys


def usage():
    print("Usage: " + sys.argv[0] + " file", file=sys.stderr)


if len(sys.argv) != 2:
    usage()
    sys.exit(1)

words = {}

fh = open(sys.argv[1])  # romeo.txt

for line in fh:
    line = line.rstrip()
    if line:
        for word in line.split(" "):
            word = word.lower()
            words[word] = words.get(word, 0)
            words[word] += 1

fh.close()

for word in sorted([word for word, count in words.items() if count is 1]):
    print(word)
