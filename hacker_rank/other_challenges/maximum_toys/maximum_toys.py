#!/usr/bin/python3
import sys

# Second day challenge


def maximumToys(prices, k):
    i = 0
    prices.sort()
    for x in range(len(prices)):
        if k < prices[x]:
            continue
        k -= prices[x]
        i += 1
    return i


if __name__ == "__main__":
    n, k = input().strip().split(" ")
    n, k = [int(n), int(k)]
    prices = list(map(int, input().strip().split(" ")))
    if (1 > n) or (n > 10**5):
        sys.exit(1)
    if (1 > k) or (k > 10**9):
        sys.exit(1)
    for a in range(len(prices)):
        if (1 > prices[a]) or (prices[a] > 10**9):
            sys.exit(1)
    result = maximumToys(prices, k)
    print(result)
