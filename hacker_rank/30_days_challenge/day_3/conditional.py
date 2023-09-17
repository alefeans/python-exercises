#!/usr/bin/python3

import sys


N = int(input().strip())

if (N > 0) and (N < 101):
    if N % 2 == 1:
        print("Weird")
    elif (N > 1) and (N < 6):
        print("Not Weird")
    elif (N > 5) and (N < 21):
        print("Weird")
    else:
        print("Not Weird")
else:
    sys.exit(1)
