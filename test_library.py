import unittest
from main import Library

class LibraryTestCases(unittest.TestCase):
    def setUp(self):
        ## Initialize a new instance of Library before each test
        self.Librarian = Library()
    ##

    def test_add_book(self):
        ## adding a book to library books
        result = self.Librarian.add_book("2", "Harry Potter", "J.K. Rowling", "1997")
        self.assertEqual(result, "Book Added Successfully!")
    ##

    def test_borrow_book(self):
        ## Borrow the book
        result = self.Librarian.borrow_book("The Alchemist")
        self.assertEqual(result, "Book Borrowed Successfully!")

        ## Attempt to borrow the same book again, which should raise an error
        with self.assertRaises(ValueError) as context:
            self.Librarian.borrow_book("The Alchemist")
        self.assertEqual(str(context.exception), 'Sorry, "The Alchemist" is currently borrowed.')
    ##

    def test_nonexistent_borrow_book(self):
        ## testing if a non-existent book can be borrowed or not!
        with self.assertRaises(ValueError) as context:
            self.Librarian.borrow_book("The Hobbit")
        self.assertEqual(str(context.exception), 'Book "The Hobbit" not found in the library.')
    ##

    def test_return_book(self):
        ## checking if book can be returned or not
        result = self.Librarian.return_book("The Alchemist")
        self.assertEqual(result, "Book Returned Successfully!")

        ## checking if available book can be returned or not
        with self.assertRaises(ValueError) as context:
            self.Librarian.return_book("The Alchemist")
        self.assertEqual(str(context.exception), 'Sorry, "The Alchemist" is already available.')
    ##

    def test_nonexistent_return_book(self):
        ## testing if a non-existent book can be returned or not!
        with self.assertRaises(ValueError) as context:
            self.Librarian.return_book("The Hobbit")
        self.assertEqual(str(context.exception), 'Book "The Hobbit" not found in the library.')
    ##


