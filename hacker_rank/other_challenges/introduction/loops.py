#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n = int(input())

    if (n < 1) and (n > 20):
        sys.exit(1)

    for i in range(n):
        print(i**2)
