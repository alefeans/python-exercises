from book import Book


class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    def display(self):
        print(
            "Title: {0}\nAuthor: {1}\nPrice: {2}".format(self.title, self.author, self.price)
        )
