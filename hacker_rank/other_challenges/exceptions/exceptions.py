#!/usr/bin/python3
import sys

t = int(input())
if (t < 1) and (t > 9):
    sys.exit(1)

for i in range(0, t):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)
