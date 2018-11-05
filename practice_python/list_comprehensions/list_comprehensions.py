def even_numbers(number_list):
    return [x for x in number_list if int(x) % 2 != 0]


if __name__ == "__main__":
    number_list = list(input("Tell me a list of numbers: ").split())
    print(even_numbers(number_list))
