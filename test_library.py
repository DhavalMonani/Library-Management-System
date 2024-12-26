import unittest
from main import Library

class LibraryTestCases(unittest.TestCase):
    def setUp(self):
        # Initialize a new instance of Library before each test
        self.Librarian = Library()
        # Add some initial books
        self.Librarian.add_book("1", "The Alchemist", "Paulo Coelho", "1988")

    def test_add_book(self):
        result = self.Librarian.add_book("2", "Harry Potter", "J.K. Rowling", "1997")
        self.assertEqual(result, "Book Added Successfully!")

    def test_borrow_book(self):
        # Borrow the book
        result = self.Librarian.borrow_book("The Alchemist")
        self.assertEqual(result, "Book Borrowed Successfully!")

        # Attempt to borrow the same book again, which should raise an error
        with self.assertRaises(ValueError) as context:
            self.Librarian.borrow_book("The Alchemist")
        self.assertEqual(str(context.exception), 'Sorry, "The Alchemist" is currently borrowed.')

