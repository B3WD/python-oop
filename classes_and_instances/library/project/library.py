from user import User
from registration import Registration
# from project.user import User
# from project.registration import Registration

class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = dict() # {author : [books]}
        self.rented_books = dict() # {user_name : { book_names : days_to_return }}

    @staticmethod
    def find_user_with_book(rented_books, book_name):
        for user in rented_books:
            if book_name in rented_books[user]:
                return user

    def get_book(self, author, book_name, days_to_return, user : User):
        if book_name not in self.books_available[author]:
            # What if book is nowhere?
            # if book_name not in user.books:
            #     return
            user_of_book = self.find_user_with_book(self.rented_books, book_name)
            days_to_return_already_rented_book = self.rented_books[user_of_book][book_name]
            return f"The book \"{book_name}\" is already rented and will be available in {days_to_return_already_rented_book} days!"
        
        Registration.add_user(user, self)

        user.books.append(book_name)
        self.books_available[author].remove(book_name)
        self.rented_books[user.username][book_name] = days_to_return
        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author, book_name, user: User):
        if book_name not in self.rented_books[user.username]:
            return f"{user.username} doesn't have this book in his/her records!"

        self.books_available[author].append(book_name)
        self.rented_books[user.username].pop(book_name)
        user.books.remove(book_name)