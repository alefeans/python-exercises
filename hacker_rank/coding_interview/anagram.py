#!/usr/bin/python3.6
import sys
import string

def number_needed(a, b):
    return len(set(a) ^ set(b))


def validate(a, b, letters):
    if (len(a) < 1) and (len(a) > 10**4):
        sys.exit(1)
    if (len(b) < 1) and (len(b) > 10**4):
        sys.exit(1)
    if (a not in letters):
        sys.exit(1)
    if (b not in letters):
        sys.exit(1)

a = input().strip()
b = input().strip()
letters = string.ascii_lowercase
validate(a, b, letters)
print(number_needed(a, b))
