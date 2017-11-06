#!/usr/bin/python3.6
import sys

def get_entry():
    n = int(input())
    if (n < 0) and (n > 10**5):
        sys.exit(1)
    else:
        return n

def get_phones(n):
    d = dict(input().split() for i in range(n))
    return d

def do_your_queries():
    t = 1
    while (t > 0) and (t < 10**5+1):
        query = input().strip()
        t += 1

def main():
    n = get_entry()
    d = get_phones(n)
    t = 1
    while (t > 0) and (t < 10**5+1):
        query = input().strip()
        
        t += 1
