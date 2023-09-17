#!/usr/bin/python3
import sys

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    if (a < 1) and (a > 10**10) and (b < 1) and (b > 10**10):
        sys.exit(1)
    print(a + b)
    print(a - b)
    print(a * b)
