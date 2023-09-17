#!/usr/bin/python3
import sys


def array_left_rotation(k, a):
    return a[k:] + a[:k]


def validator(n, k, a):
    if (n < 1) and (n > 10**5):
        sys.exit(1)
    elif (k < 1) and (k > n):
        sys.exit(1)
    elif (len(a) < 1) and (len(a) > 10**6):
        sys.exit(1)
    else:
        return


n, k = map(int, input().strip().split(" "))
a = list(map(int, input().strip().split(" ")))
validator(n, k, a)
answer = array_left_rotation(k, a)
print(*answer, sep=" ")
