# library_management.py

class Book:
    """A class representing a book with title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is currently available."""
        return not self._is_checked_out


class Library:
    """A class that stores and manages a collection of books."""

    def __init__(self):
        self._books = []  # private list

    def add_book(self, book):
        """Add a new Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"No book found with title '{title}'.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"No book found with title '{title}'.")

    def list_available_books(self):
        """Print a list of all available books."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books available.")
            return

        for book in available:
            print(f"{book.title} by {book.author}")
