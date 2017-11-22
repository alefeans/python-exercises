#!/usr/bin/python3
import person

t = int(input())
for i in range(t):
    age = int(input())
    p = person.Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
