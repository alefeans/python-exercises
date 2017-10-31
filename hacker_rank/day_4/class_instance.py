#!/usr/bin/python3.6
import p_person

t = int(input())
for i in range(0, t):
    age = int(input())
    p = p_person.Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
