import unittest
from Library import Library

class LibraryTestCases(unittest.TestCase):
    def setUp(self):
        ## Initialize a new instance of Library before each test
        self.Librarian = Library()
        result = self.Librarian.add_user("1","Dhaval","Librarian")
        self.assertEqual(result,"User added successfully!")
        result = self.Librarian.add_user("2","John")
        self.assertEqual(result,"User added successfully!")
    ##

    # def test_add_user(self):

    #     result = self.Librarian.add_user("2","John")
    #     self.assertEqual(result,"User added successfully!")
    # ##

    def test_add_book(self):
        ## adding a book to library books
        result = self.Librarian.add_book("1","2", "Harry Potter", "J.K. Rowling", "1997")
        self.assertEqual(result, "Book Added Successfully!")
    ##

    def test_borrow_book(self):
        ## Borrow the book
        result = self.Librarian.borrow_book("2","The Alchemist")
        self.assertEqual(result, "Book Borrowed Successfully!")

        ## Attempt to borrow the same book again, which should raise an error
        with self.assertRaises(ValueError) as context:
            self.Librarian.borrow_book("2","The Alchemist")
        self.assertEqual(str(context.exception), 'Sorry, "The Alchemist" is currently borrowed.')
    ##

    # def test_nonexistent_borrow_book(self):
    #     ## testing if a non-existent book can be borrowed or not!
    #     with self.assertRaises(ValueError) as context:
    #         self.Librarian.borrow_book("The Hobbit")
    #     self.assertEqual(str(context.exception), 'Book "The Hobbit" not found in the library.')
    # ##

    # def test_return_book(self):
    #     ## checking if book can be returned or not
    #     result = self.Librarian.return_book("The Alchemist")
    #     self.assertEqual(result, "Book Returned Successfully!")

    #     ## checking if available book can be returned or not
    #     with self.assertRaises(ValueError) as context:
    #         self.Librarian.return_book("The Alchemist")
    #     self.assertEqual(str(context.exception), 'Sorry, "The Alchemist" is already available.')
    # ##

    # def test_nonexistent_return_book(self):
    #     ## testing if a non-existent book can be returned or not!
    #     with self.assertRaises(ValueError) as context:
    #         self.Librarian.return_book("The Hobbit")
    #     self.assertEqual(str(context.exception), 'Book "The Hobbit" not found in the library.')
    # ##

    # def test_available_books(self):
    #     ## expected books will be compared with available books
    #     expected_books = [{"ISBN": "1", "title": "The Alchemist", "author": "Paulo Coelho", "publication_year": "1988", "status": "available"}]
    #     available_books = self.Librarian.view_available_books() ##calling the method for getting output
    #     self.assertEqual(available_books,expected_books) ##comparing both the outputs
    # ##
 