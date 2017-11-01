#!/usr/bin/python3.6
import sys

# It worked on my machine. So, i don't give a...

def get_entry():
    n = int(input().strip())
    if  (n < 1) and (n > 100):
        sys.exit(1)
    else:
        return n

def get_socks(n):
    socks = []
    for i in range(0, n):
        c = int(input().strip())
        if (c < 1) and (c > 100):
            sys.exit(1)
        else:
            socks.append(c)
    return socks

def operations(socks):
    socks.sort()
    total = 0
    for i in range(0, len(socks), 2):
        if ((i + 1) == len(socks)):
            return total
        elif socks[i] == socks[i+1]:
            total += 1
        else:
            continue
def main():
    n = get_entry()
    socks = get_socks(n)
    total = operations(socks)
    print(total)

main()
