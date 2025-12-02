# library_system.py

class Book:
    """Base class representing a generic book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        """Return basic info for a regular book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Electronic book with an extra file_size attribute."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def get_info(self):
        """Return info specific to ebooks."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Printed book with an extra page_count attribute."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_info(self):
        """Return info specific to printed books."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Holds a collection of books (Book, EBook, PrintBook)."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a book instance to the library collection."""
        self.books.append(book)

    def list_books(self):
        """Print information for each book in the library in insertion order."""
        for book in self.books:
            print(book.get_info())
