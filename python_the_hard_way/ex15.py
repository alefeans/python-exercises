#!/usr/bin/env python3
import os

while True:
    filename = input("Digite o path/arquivo: ")
    try:
        txt = open(filename,'r')
        break
    except(IOError, ValueError):
        print("Tente novamente...")
print(txt.read())
txt.close()
