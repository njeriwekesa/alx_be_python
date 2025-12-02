# library_system.py

class Book:
    """Base class representing a general book."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        """Return information about the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def get_info(self):
        """Return EBook information (overrides base method)."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a physical printed book."""

    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_info(self):
        """Return PrintBook information (overrides base method)."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class demonstrating composition by storing books."""

    def __init__(self):
        self.books = []  # List of Book, EBook, or PrintBook instances

    def add_book(self, book):
        """Add a book to the library."""
        self.books.add(book) if isinstance(self.books, set) else self.books.append(book)

    def list_books(self):
        """Print information about each book in the library."""
        for book in self.books:
            print(book.get_info())
