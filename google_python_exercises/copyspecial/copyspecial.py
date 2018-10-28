#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
"""Copy Special exercise

* Takes one or more directories as argument * A special file is where the name
  contains the pattern __w__ somewhere, where w is one or more word characters

"""

# +++your code here+++
# Write functions and modify main() to call them


def get_special_paths(dir):
    paths = []
    if os.path.isdir(dir):
        for file in os.listdir(dir):
            if re.search(r"__\w+__", file):
                path = "{}/{}".format(dir, file)
                paths.append(os.path.abspath(path))
    return paths


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    # +++your code here+++
    # Call your functions
    for dir in sys.argv[1:]:
        get_special_paths(dir)


if __name__ == "__main__":
    main()
