import datetime


def years(name, age):
    yrs = datetime.datetime.now()
    yrs = (yrs.year - age) + 100
    return f"{name} will be 100 years old in {yrs}"


if __name__ == "__main__":
    name = input("What's your name ? ")
    age = int(input("What's your age ? "))
    print(years(name, age))
    number = int(input("Tell me a number: "))
    for i in range(number):
        print(years(name, age))
