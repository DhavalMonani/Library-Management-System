import unittest
import add_books from main

class LibraryTestCases(unittest.TestCase):
    
    def test_add_books(self):
        result = add_books("1", "The Alchemist", "Paulo Coelho", "1988")
        self.assertEqual(result,"Book Added Successfully!")
    ##
