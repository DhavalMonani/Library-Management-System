import unittest
from main import Library

class LibraryTestCases(unittest.TestCase):
    def setUp(self):
        self.Librarian = Library()
    ##

    def test_add_book(self):
        result = self.Librarian.add_book("2", "Harry Potter", "J.K. Rowling", "1997")
        self.assertEqual(result,"Book Added Successfully!")
    ##

    def test_borrow_book(self):
        result = self.Librarian.borrow_book("The Alchemist")
        self.assertEqual(result,"Book Borrowed Successfully!")
    ##

    def test_borrow_book2(self):
        with self.assertRaises(ValueError) as context:
            self.Librarian.borrow_book("The Alchemist")
        self.assertEqual(str(context.exception), 'Sorry, "The Alchemist" is currently borrowed.')
    ##


