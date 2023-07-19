
class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title


class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

    def display_info(self):
        print("Member ID:", self.member_id)
        print("Name:", self.name)
        print("Borrowed Books:")
        for book in self.borrowed_books:
            print("Book ID:", book.book_id, ", Title:", book.title)


class ExtendedLibraryMember(LibraryMember):
    def __init__(self, member_id, name, max_books):
        super().__init__(member_id, name)
        self.max_books = max_books

    def borrow_book(self, book):
        if len(self.borrowed_books) < self.max_books:
            self.borrowed_books.append(book)
            print("Book borrowed successfully.")
        else:
            print("Maximum number of books borrowed. Cannot borrow more.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print("Book returned successfully.")
        else:
            print("Book not found in borrowed books.")


