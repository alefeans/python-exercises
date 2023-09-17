#!/usr/bin/python3

arr = []
for i in range(6):
    arr_t = [int(j) for j in input().strip().split(" ")]
    arr.append(arr_t)

total = []
for x in range(0, 4):
    for y in range(0, 4):
        s = sum(arr[x][y : y + 3]) + arr[x + 1][y + 1] + sum(arr[x + 2][y : y + 3])
        total.append(s)

print(max(total))
