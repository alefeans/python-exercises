#!/usr/bin/python3
import sys


class Difference:
    def __init__(self, a):
        self.__elements = a
        if (len(self.__elements) < 1) and (len(self.__elements) > 10):
            sys.exit(1)
        if (max(self.__elements) > 100) and (min(self.__elements) < 1):
            sys.exit(1)

    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)


_ = input()
a = [int(e) for e in input().split(" ")]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
