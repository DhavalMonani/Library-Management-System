import unittest
from main import Library

class LibraryTestCases(unittest.TestCase):
    
    def test_add_books(self):
        Librarian = Library()
        result = Librarian.add_books("1", "The Alchemist", "Paulo Coelho", "1988")
        self.assertEqual(result,"Book Added Successfully!")
    ##
