def response(number):
    if number % 4 == 0:
        return "Multiple of four"
    elif number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def divisible(num, check):
    if check % num == 0:
        return "Yes, it's evenly divisible"
    return "No, it's not evenly divisible"


if __name__ == "__main__":
    number = int(input("Tell me a number: "))
    print(response(number))
