class Library:

    def __init__(self):
         ## default book
         self.books = [{"ISBN": "1", "title": "The Alchemist", "author": "Paulo Coelho", "publication_year": "1988", "status": "available"}]
    ##

    def add_book(self, isbn, title, author, publication_year):
        ## creating a dictionary for the new book and default status 'available'
        new_book = {
            "ISBN": isbn,
            "title": title,
            "author": author,
            "publication_year": publication_year,
            "status": "available"
        }
        ## adding the book inside the list
        self.books.append(new_book)
        return "Book Added Successfully!"
    ##

    def borrow_book(self, title):
        ## searching for the book inside the books list
        for book in self.books:
            if book["title"].lower() == title.lower(): ## checking if book title are same or not
                if book["status"] == "available":
                    book["status"] = "borrowed" ## updating the status for the book
                    return "Book Borrowed Successfully!"
                else:
                    raise ValueError(f'Sorry, "{title}" is currently borrowed.') ## raising error if borrowed book is being borrowed again
        raise ValueError(f'Book "{title}" not found in the library.') ## raising error if an unknown book is being requested for borrowing

    def return_book(self,title):
        ## checking if book is available or not
        for book in self.books:
            if book["title"].lower() == title.lower():
                if book["status"] == "borrowed":
                    book["status"] = "available" ## updating the status of the book
                    return "Book Returned Successfully!"
                else:
                    raise ValueError(f'Sorry, "{title}" is already available.') ##raising error if book is already available
        raise ValueError(f'Book "{title}" not found in the library.') ## raising error if book is not found!
    ##

    def view_available_books(self):
        pass
    ##

##