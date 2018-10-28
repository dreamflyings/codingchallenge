#!/usr/bin/env python3

import socket
import sys


def usage():
    print("Usage: " + sys.argv[0] + " url", file=sys.stderr)


if len(sys.argv) != 2:
    usage()
    sys.exit(1)

url = sys.argv[1]

addr = url.split("/")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((addr[2], 80))
    s.send("GET {} HTTP/1.0\n\n".format(url).encode())

    while True:
        data = s.recv(512)
        if len(data) < 1:
            break
        print(data)

    s.close()
except:
    raise Exception("Likely malformed URL")
