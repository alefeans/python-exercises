#!/usr/bin/python3
from my_book import MyBook

title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
