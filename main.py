class Library:

    def __init__(self):
         self.books = [{"ISBN": "1", "title": "The Alchemist", "author": "Paulo Coelho", "publication_year": "1988", "status": "available"}]
    ##

    def add_book(self, isbn, title, author, publication_year):
        new_book = {
            "ISBN": isbn,
            "title": title,
            "author": author,
            "publication_year": publication_year,
            "status": "available"
        }
        self.books.append(new_book)
        return "Book Added Successfully!"
    ##

    def borrow_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                if book["status"] == "available":
                    book["status"] = "borrowed"
                    return "Book Borrowed Successfully!"
                else:
                    raise ValueError(f'Sorry, "{title}" is currently borrowed.')
        raise ValueError(f'Book "{title}" not found in the library.')

    def return_book(self):
        pass
    ##

    def view_available_books(self):
        pass
    ##

##