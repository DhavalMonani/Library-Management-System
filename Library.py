from user import User
from validate_data import validate_details
class Library:

    def __init__(self):
         ## all the books in library
         self.books = []

         ## Dictionary of users with user_id as key
         self.users = {}
    ##

    def add_user(self,user_id,username,role="user"):
        # Validate each detail
        validate_details(user_id)
        validate_details(username)
        if user_id in self.users:
            raise ValueError(f"User ID {user_id} already exists.")
        self.users[user_id] = User(user_id, username, role)
        return "User added successfully!"
    ##

    def add_book(self,user_id, isbn, title, author, publication_year):
            # Validate each detail
            validate_details(user_id)
            validate_details(isbn)
            validate_details(title)
            validate_details(author)
            validate_details(publication_year)

            ## check if user is valid or not
            if user_id not in self.users or self.users[user_id].role != "Librarian":
                raise ValueError("Only Librarian can add books.")
            else:
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

    def borrow_book(self,user_id,title):
        # Validate each detail
        validate_details(user_id)
        validate_details(title)

        ## validating the user
        if user_id not in self.users:
            raise ValueError("User Not Found!")
        else:
            ## getting user data with user_id from self.users
            user = self.users[user_id]

            ## searching for the book inside the books list
            for book in self.books:
                if book["title"].lower() == title.lower(): ## checking if book title are same or not
                    if book["status"] == "available":
                        book["status"] = "borrowed" ## updating the status for the book
                        user.borrowed_books.append(title)## adding the book in user's borrowed book list
                        return "Book Borrowed Successfully!"
                    else:
                        raise ValueError(f'Sorry, "{title}" is currently borrowed.') ## raising error if borrowed book is being borrowed again
            raise ValueError(f'Book "{title}" not found in the library.') ## raising error if an unknown book is being requested for borrowing
    ##

    def return_book(self,user_id,title):
        # Validate each detail
        validate_details(user_id)
        validate_details(title)

        ## validating the user
        if user_id not in self.users:
            raise ValueError("User Not Found!")
        else:
            ## checking if book has been borrowed or not
            user = self.users[user_id]
            if title not in user.borrowed_books:
                raise ValueError('User has not borrowed this Book.')
            else:
                for book in self.books:
                    if book["title"].lower() == title.lower():
                        if book["status"] == "borrowed":
                            book["status"] = "available" ## updating the status of the book
                            user.borrowed_books.remove(title) ##removing book from user's borrowed books
                            return "Book Returned Successfully!"
    ##

    def view_available_books(self):
        return [book for book in self.books if book["status"] == "available"]
    ##

    def view_user(self,user_id):
        # Validate each detail
        validate_details(user_id)

        if user_id not in self.users:
            raise ValueError(f"User ID {user_id} does not exist.")
        return str(self.users[user_id])
    ##

    def view_all_user(self,user_id):
        # Validate each detail
        validate_details(user_id)

        if self.users[user_id].role != "Librarian":
            raise ValueError("Only admins can view all users.")
        return [str(user) for user in self.users.values() if user.role != "Librarian"]
##