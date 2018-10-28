#!/usr/bin/env python3
"""
* split using re.split, delimeter is {}, use () to capture the delim
* iterate over tokens, if startswith { then expand
"""

from itertools import product
import re


def iscurly(x):
    return x.startswith("{") and x.endswith("}")


def cartesian_product_ii(s):
    tokens = [x for x in re.split("({[\w+,]+})", s)]
    # ['00', '{a,b}', '11', '{c,d}', '', '{e,f}', '33', '{g,h}', '44']

    l = len(tokens)

    # prefix
    prefix = ""
    if l > 0:
        t = tokens[0]
        if not iscurly(t):
            prefix = t
            tokens = tokens[1:]

    # suffix
    suffix = ""
    if l > 1:
        t = tokens[-1]
        if not iscurly(t):
            suffix = t
            tokens = tokens[:-1]

    middle = ""

    partials = []
    for t in tokens:
        if not iscurly(t):
            middle = t
        elif iscurly(t):
            x = [middle + i for i in t[1:-1].split(",")]
            partials.append(x)
            middle = ""

    print(partials)
    for pp in product(*partials):
        print(prefix + "".join(pp) + suffix)


cartesian_product_ii("00{a,b}11{c,d}22{e,f}33{g,h}44")
