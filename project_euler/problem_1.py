def multiples_sum():
    return sum([i for i in range(3, 1000) if (i % 3 == 0) or (i % 5 == 0)])


if __name__ == "__main__":
    print(multiples_sum())
