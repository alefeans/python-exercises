#!/usr/bin/python3
import sys


def factorial(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return factorial(n - 1) * n


if __name__ == "__main__":
    n = int(input().strip())
    if (n < 2) and (n > 12):
        sys.exit(1)

    result = factorial(n)
    print(result)
