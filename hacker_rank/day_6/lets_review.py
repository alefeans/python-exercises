#!/usr/bin/python3.6
import sys

def getEntry():
    t = int(input().strip())
    if (t < 1) and (t > 10):
        sys.exit(1)
    else:
        return t

def getStrings(t):
    s = input().strip()
    if (len(s) < 2) and (len(s) > 10000):
        sys.exit(1)
    else:
        return s

def splitString(s):
    test = list(s)
    lista_par = ""
    lista_impar = ""
    for i in range(0, len(s)):
        if (i % 2 == 0):
            lista_par += s[i]
        else:
            lista_impar += s[i]
    lista_final = lista_par, lista_impar
    return lista_final

def showMessage(lista_final):
    print(lista_final[0], lista_final[1])


t = getEntry()
for i in range(0, t):
    s = getStrings(t)
    lista_final = splitString(s)
    showMessage(lista_final)
