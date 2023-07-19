class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.borrowed = False
    def borrow_book(self):
        self.borrowed = True
    def return_book(self):
        self.borrowed = False
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication year: {self.publication_year}")
        print(f"Borrowed: {self.borrowed}")