"""
Requirements:
an user should add/remove books from their library
an user should set a book from the library as actiev
the system should remember where a user left off in a given book
the system only displays a page of text at a time in the active book

Classes:
    Book:
        - id: int
        - author: str
        - content: str
        - active_page: int
        - pages: [str]

    Library:
        - books: Dict[int, Book]
        - active_book: int
"""
from typing import Dict


class Book:
    def __init__(
        self, id: int, author: str, content: str, chars_limit_per_page: int = 5
    ) -> None:
        self.id = id
        self.author = author
        self.active_page = 0
        self.pages = [
            content[i : i + chars_limit_per_page]
            for i in range(0, len(content), chars_limit_per_page)
        ]

    def turn_page(self) -> str:
        next_page = self.pages[self.active_page + 1]
        self.active_page += 1
        return next_page

    def show_page(self) -> str:
        return self.pages[self.active_page]


class Library:
    def __init__(self) -> None:
        self.books: Dict[int, Book] = dict()
        self.active_book = -1

    def add_book(self, book: Book) -> None:
        self.books[book.id] = book

    def remove_book(self, id: int) -> None:
        self.books.pop(id)

    def set_active_book(self, id: int) -> None:
        self.active_book = id

    def get_active_book(self) -> Book:
        return self.books[self.active_book]


if __name__ == "__main__":
    book_1 = Book(0, "Me", "Lalalalalalalal allalala")
    my_lib = Library()
    my_lib.add_book(book_1)
    my_lib.set_active_book(0)
    active_book = my_lib.get_active_book()
    print(active_book.show_page())
    print(active_book.turn_page())
    print(active_book.turn_page())
    print(active_book.turn_page())
    print(active_book.turn_page())
