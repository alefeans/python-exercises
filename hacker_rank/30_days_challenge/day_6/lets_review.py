#!/usr/bin/python3
import sys


# Valida se a quantidade de testes está ok (1 até 10 testes)
def get_entry():
    t = int(input().strip())
    if (t < 1) and (t > 10):
        sys.exit(1)
    else:
        return t


# Valida se a string informada possui o tamanho correto (2 até 10000)
def get_strings():
    s = input().strip()
    if (len(s) < 2) and (len(s) > 10000):
        sys.exit(1)
    else:
        return s


# Faz uma iteração na string informada, incluindo os caracteres pares na "lista" par
# (even) e os caracteres ímpares na "lista" impar (odd). Ao final, inclui a "lista" par
# no índice 0 e inclui a "lista" impar no índice 1 da "lista" final.
def split_string(s):
    even = ""
    odd = ""
    for i in range(len(s)):
        if i % 2 == 0:
            even += s[i]
        else:
            odd += s[i]
    final = even, odd
    return final


def main():
    t = get_entry()
    for i in range(t):
        s = get_strings()
        final = split_string(s)
        print(*final)


main()
