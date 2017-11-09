#!/usr/bin/python3.6
import sys
import re

t = int(input())
if (t < 1) and (t > 99):
    sys.exit(1)

for i in range(t):
    try:
        s = input()
        p = re.compile(s)
        print("True")
    except:
        print("False")
