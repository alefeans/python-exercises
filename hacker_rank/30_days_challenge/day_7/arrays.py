#!/usr/bin/python3.6

import sys

n = int(input().strip())

if (n < 0) and (n > 1000):
    sys.exit(1)

arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for i in range(0, len(arr)):
    if (arr[i] < 0 ) and (arr[i] > 10000):
        sys.exit(1)

arr.reverse()
print(*arr)
