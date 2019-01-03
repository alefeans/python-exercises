def fibonacci():
    a, b = 3, 5
    total = 2
    for i in range(1, 30):
        a, b = b, a + b
        if a % 2 == 0:
            total += a
    return total


if __name__ == "__main__":
    print(fibonacci())
