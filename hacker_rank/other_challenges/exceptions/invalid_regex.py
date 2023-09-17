#!/usr/bin/python3
import re
import sys

t = int(input())
if (t < 1) and (t > 99):
    sys.exit(1)

for i in range(t):
    try:
        s = input()
        p = re.compile(s)
        print("True")
    except Exception:
        print("False")
