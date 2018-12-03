def common_numbers(list_one, list_two):
    return set(list_one) & set(list_two)


if __name__ == "__main__":
    list_one = list(input("Give me a list of numbers: "))
    list_two = list(input("Give me a second list of numbers: "))
    print(common_numbers(list_one, list_two))
