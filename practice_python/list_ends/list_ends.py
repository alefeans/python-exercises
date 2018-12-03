def cut(numbers):
    return [numbers[x] for x in range(len(numbers)) if x == 0 or x == len(numbers) - 1]


if __name__ == "__main__":
    numbers = input("Tell me a list of numbers: ")
    print(cut(numbers))
