from user import User
# from project.user import User

class Registration:
    @staticmethod
    def add_user(user : User, library):# : Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)
        library.rented_books[user.username] = dict()

    @staticmethod
    def remove_user(user : User, library):# : Library):
        if user not in library.user_records:
            return f"We could not find such user to remove!"

        library.user_records.remove(user)

    @staticmethod
    def find_user_by_id(user_id : int, library):# : Library) -> User:
        for user in library.user_records:
            if user_id == user.user_id:
                return user

    @staticmethod # static, so that there is no implicit "self"
    def get_user_ids(library):# : Library):
        return [user.user_id for user in library.user_records]

    def change_username(self, user_id : int, new_username : str, library):# : Library):
        if user_id not in self.get_user_ids(library):
            return f"There is no user with id = {user_id}!"

        user_to_change = self.find_user_by_id(user_id, library)
        if user_to_change.username == new_username:
            return f"Please check again the provided username - it should be different than the username used so far!"

        a = library.rented_books[user_to_change.username]

        library.rented_books[new_username] = library.rented_books.pop(user_to_change.username)
        user_to_change.username = new_username # Does this change affect "library.user_records?"

        return f"Username successfully changed to: {new_username} for user id: {user_id}"


        
