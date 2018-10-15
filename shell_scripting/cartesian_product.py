#!/usr/bin/env python3

from itertools import product

def cartesian_product(input):
  # search for prefix
  prefix = ""
  for ch in input:
    if ch == '{':
      break
    else:
      prefix += ch

  # search for suffix
  suffix = ""
  for ch in reversed(input):
    if ch == '}':
      break
    else:
      suffix += ch
  suffix = suffix[::-1]

  # trim prefix and suffix
  if len(prefix) > 0:
    input = input[len(prefix):]
  if len(suffix) > 0:
    input = input[:-len(suffix)]

  # parse for sets and delimiters
  first = False
  inside = False
  delims = []
  delim = ""
  sets = []
  set = ""

  for ch in input:
    if inside: set += ch
    else: delim += ch

    if ch == '{':
      inside = True
      if not first:
        delim = delim[0:-1]
        if delim: delims.append(delim)
        delim = ""
      first = False
    elif ch == '}':
      inside = False
      if set:
        sets.append(set[0:-1].split(","))
        set = ""

  if len(delims) > 1:
    raise Exception("0 or 1 delimiters only")

  if len(sets) != 2:
    raise Exception("2 sets only")

  if delims:
    sets[0] = list(map(lambda x: x+delims[0], sets[0]))

  ans = []
  for i in product(sets[0], sets[1]):
    ans.append(prefix+"".join(i)+suffix)
  ans = " ".join(ans)

  return ans

cartesian_product("_PF{a,b}UV{1,2}SF_") # echo "_PF{a,b}UV{1,2}SF_"
cartesian_product("_PF{a,b}{1,2}SF_")
cartesian_product("{a,b}!{1,2}SF_")
cartesian_product("_PF{a,b}!{1,2}")
cartesian_product("{a,b}{1,2}SF_")
cartesian_product("_PF{a,b}UV{1,2}")
cartesian_product("{a,b}{1,2}")

