class User:
    def __init__(self,user_id,username,role="user"):
        self.user_id = user_id
        self.username = username
        self.role = role
        self.borrowed_books = []
    ##
    def __str__(self):
        return f"User ID: {self.user_id}, Username: {self.username}, Role: {self.role}, Borrowed Books: {self.borrowed_books}"
     