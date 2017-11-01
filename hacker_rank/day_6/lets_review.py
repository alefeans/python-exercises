#!/usr/bin/python3.6
import sys

# Valida se a quantidade de testes está ok (1 até 10 testes)
def getEntry():
    t = int(input().strip())
    if (t < 1) and (t > 10):
        sys.exit(1)
    else:
        return t

# Valida se a string informada possui o tamanho correto (2 até 10000)
def getStrings():
    s = input().strip()
    if (len(s) < 2) and (len(s) > 10000):
        sys.exit(1)
    else:
        return s

# Faz uma iteração na string informada, incluindo os caracteres pares na "lista" par
# (even) e os caracteres ímpares na "lista" impar (odd). Ao final, inclui a "lista" par
# no índice 0 e inclui a "lista" impar no índice 1 da "lista" final.
def splitString(s):
    even = ""
    odd = ""
    for i in range(0, len(s)):
        if (i % 2 == 0):
            even += s[i]
        else:
            odd += s[i]
    final = even, odd
    return final

def main():
    t = getEntry()
    for i in range(0, t):
        s = getStrings()
        final = splitString(s)
        print(final[0], final[1])

main()
