#!/usr/bin/python3
import sys

n = int(input().strip())
if (n < 2) or (n > 20):
    sys.exit(1)
else:
    for i in range(1, 11):
        t = i * n
        print(n, "x", i, "=", t)
