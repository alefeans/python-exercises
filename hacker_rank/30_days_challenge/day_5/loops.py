#!/usr/bin/python3
import sys


n = int(input().strip())

if (n < 2) or (n > 20):
    sys.exit(1)

i = 1
while (i > 0) and (i < 11):
    t = i * n
    print(n, "x" , i , "=" , t)
    i += 1
