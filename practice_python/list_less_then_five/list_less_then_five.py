def check_list(lista):
    return [lista[i] for i in range(len(lista)) if lista[i] < 5]


if __name__ == "__main__":
    l = input("Give me a list of numbers: ")
    lista = list(map(int, l.split()))
    print(check_list(lista))
