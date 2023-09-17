#!/usr/bin/python3

import sys

n = int(input().strip())

if (n < 0) and (n > 1000):
    sys.exit(1)
else:
    arr = [int(t) for t in input().strip().split(" ")]
    for i in range(len(arr)):
        if (arr[i] < 0) and (arr[i] > 10000):
            sys.exit(1)

arr.reverse()
print(*arr)
