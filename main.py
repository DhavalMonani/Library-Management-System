class Library:

    def __init__(self):
        self.books = []
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

    def borrow_book(self):
        pass
    ##

    def return_book(self):
        pass
    ##

    def view_available_books(self):
        pass
    ##

##