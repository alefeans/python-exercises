#!/usr/bin/python3
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


def do_your_queries(d, query):
    if (query in d) is True:
        print("{0}={1}".format(query, d[query]))
    else:
        print("Not found")


def repeating(d):
    t = 1
    while (t > 0) and (t < 10**5 + 1):
        query = input().strip()
        do_your_queries(d, query)
        t += 1


def main():
    n = get_entry()
    d = get_phones(n)
    repeating(d)


if __name__ == "__main__":
    main()
