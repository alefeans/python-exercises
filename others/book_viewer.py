"""
Requirements:
a user should add/remove books from their library 
a user should set a book from the library as active 
the system should remember where a user left off in a given book 
the system only displays a page of text at a time in the active book 

Solution Design:
Classes:
    Book:
        - id: int
        - author: str
        - content: str

    Library:
        - books: Dict[int, Book]

    Display:
        - library: Library
        - active_book: int
        - active_page: int
        - active_book_pages: List[str]
        - chars_limit_per_page: int
"""
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(frozen=True)
class Book:
    id: int
    author: str
    content: str


@dataclass
class Library:
    books: Dict[int, Book] = field(default_factory=dict)

    def add_book(self, book: Book) -> None:
        self.books[book.id] = book

    def remove_book(self, id: int) -> None:
        self.books.pop(id, None)


@dataclass
class Display:
    library: Library
    active_book: int = -1
    active_page: int = 0
    active_book_pages: List[str] = field(default_factory=list)
    chars_limit_per_page: int = 12

    def add_book(self, book: Book) -> None:
        return self.library.add_book(book)

    def remove_book(self, id: int) -> None:
        if self.active_book == id:
            self.active_book = -1
            self.active_page = 0
            self.active_book_pages = []
        return self.library.remove_book(id)

    def choose_book(self, id: int) -> Book | None:
        book = self.library.books.get(id)
        if book:
            self.active_book = id
            self.active_book_pages = self.get_active_book_pages()
        return book

    def get_active_book(self) -> Book | None:
        return self.library.books.get(self.active_book, None)

    def get_active_book_pages(self) -> List[str]:
        active_book = self.get_active_book()
        if active_book is None:
            return []

        content_length = len(active_book.content)
        for chunk_size in range(0, content_length, self.chars_limit_per_page):
            self.active_book_pages.append(
                active_book.content[chunk_size : chunk_size + self.chars_limit_per_page]
            )
        return self.active_book_pages

    def get_active_page(self) -> str:
        if not self.active_book_pages:
            return ""
        return self.active_book_pages[self.active_page]

    def turn_page(self) -> str:
        book = self.get_active_book()
        last_page_number = len(self.active_book_pages) - 1
        if not book or self.active_page == last_page_number:
            return ""

        self.active_page += 1
        return self.active_book_pages[self.active_page]


if __name__ == "__main__":
    book_1 = Book(
        1,
        "Guido",
        "The value of some objects can change. Objects whose value can change are said to be \
        mutable; objects whose value is unchangeable once they are created are called \
        immutable. (The value of an immutable container object that contains a reference to a \
        mutable object can change when the latters value is changed; however the container is \
        still considered immutable, because the collection of objects it contains cannot be \
        changed. So, immutability is not strictly the same as having an unchangeable value, \
        it is more subtle.) An object’s mutability is determined by its type; for instance, \
        numbers, strings and tuples are immutable, while dictionaries and lists are mutable.",
    )
    book_2 = Book(
        2,
        "Oduig",
        "Objects are Python’s abstraction for data. All data in a Python program is \
        represented by objects or by relations between objects. (In a sense, and in \
        conformance to Von Neumann’s model of a “stored program computer”, code is \
        also represented by objects.)",
    )

    library = Library()
    library.add_book(book_1)
    library.add_book(book_2)
    display = Display(library, chars_limit_per_page=22)
    print(display.get_active_book())
    display.choose_book(2)
    print(display.get_active_book())
    print(display.get_active_page())
    print(display.turn_page())
    print(display.turn_page())
    print(display.turn_page())
    print(display.turn_page())
    print(display.turn_page())
    print(display.turn_page())
    print(display.turn_page())
    print(display.turn_page())
    display.remove_book(2)
    print(display.get_active_book())
    print(display.turn_page())
    print(display.turn_page())
    print(display.turn_page())
