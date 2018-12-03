def is_palindrome(word):
    if word == word[::-1]:
        return "Is palindrome"
    return "Is not a palindrome"


if __name__ == "__main__":
    word = input("Tell me a word: ")
    print(is_palindrome(word))
