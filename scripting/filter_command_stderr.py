#!/usr/bin/env python3

import os
from subprocess import Popen, PIPE, DEVNULL, STDOUT
import sys

def usage():
    print("Usage: " + sys.argv[0] + " \"command --with args\"", file=sys.stderr)
    print("Example:")
    print('$ ./filter_command_stderr.py  "find / -name \"*.h\""')

if len(sys.argv) != 2:
    usage()
    sys.exit(1)

command = sys.argv[1].split(" ")

# os.system("".join(sys.argv[1:])) # doesn't capture output
# subprocess.run(["ls", "-l"]) # also doesn't capture output
# p = Popen(command, stdout=PIPE, stderr=DEVNULL) # output buffered in memory
# out, err = p.communicate()

# does not buffer (!)
p = Popen(command, stdout=PIPE, stderr=DEVNULL)

while True:
    line = p.stdout.readline()
    if not line: break
    sys.stdout.write(line.decode('utf-8'))
    sys.stdout.flush()

sys.exit(p.returncode)

