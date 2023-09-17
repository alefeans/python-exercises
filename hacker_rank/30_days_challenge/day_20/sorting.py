#!/usr/bin/python3
import sys

# Oh sort().. how i miss u


def validator(n, a):
    if (n < 2) and (n > 600):
        sys.exit(1)
    for i in range(len(a)):
        if (a[i] < 1) and (a[i] < 2 * 10**6):
            sys.exit(1)


def bubble_sort(a):
    swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
        if swaps == 0:
            break
    return swaps, a


n = int(input().strip())
a = list(map(int, input().strip().split(" ")))
validator(n, a)
swaps, a = bubble_sort(a)
print("Array is sorted in {} swaps.".format(swaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[n - 1]))
