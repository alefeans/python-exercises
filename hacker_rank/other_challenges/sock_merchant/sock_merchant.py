#!/usr/bin/python3
import sys


def validate_entry():
    n = int(input())
    if (n < 1) and (n > 100):
        sys.exit(1)
    else:
        return n


def validate_socks(n):
    c = [int(i) for i in input().split()]
    if len(c) > n:
        sys.exit(1)
    if (min(c) < 1) and (max(c) > 100):
        sys.exit(1)
    else:
        return c


def get_pairs(c):
    b = list(set(c))
    total = 0
    for i in range(0, len(b)):
        t = c.count(b[i])
        total += t // 2
    print(total)


def main():
    n = validate_entry()
    c = validate_socks(n)
    get_pairs(c)


main()
