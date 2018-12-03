def reverse(phrase):
    return phrase.split()[::-1]


if __name__ == "__main__":
    phrase = input("Tell me the words to reverse: ")
    print(*reverse(phrase))
