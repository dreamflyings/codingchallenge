#!/usr/bin/env python3

import sys

def usage():
    print("Usage: " + sys.argv[0] + " infile", file=sys.stderr)

if len(sys.argv) != 2:
    usage()
    sys.exit(1)

infile = open(sys.argv[1])

def remove_not_alpha(word):
    return "".join([char for char in word if char.isalpha()])

unique = {}

for line in infile:
    line = line.strip()
    if line:
        words = [remove_not_alpha(word) for word in line.split(" ")]
        for word in words:
            if not word in unique:
                unique[word] = 1
            else:
                unique[word] += 1

unique_words = [word for word, count in unique.items() if count == 1]

for word in unique_words:
    print(word)

sys.exit(0)

