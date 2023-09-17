#!/usr/bin/python3
import sys


def get_entry():
    n = int(input().strip())
    if (n < 0) and (n > 10**6):
        sys.exit(1)
    else:
        return n


def dec_to_bin(n):
    binary = bin(n)
    return binary[2:]


def counting_bin(binary):
    total = 1
    total_list = []
    test = list(map(int, binary))
    for i in range(len(test) - 1):
        if (test[i] == 1) and (test[i + 1] == 1):
            total += 1
            total_list.append(total)
        else:
            total = 1
            total_list.append(total)
    print(max(total_list))


def main():
    n = get_entry()
    binary = dec_to_bin(n)
    counting_bin(binary)


if __name__ == "__main__":
    main()
