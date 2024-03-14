import re

class UserManagement:
    def __init__(self):
        self.users = {}
        self.logged_in_users = []

    def register(self, username, password):
        if not self.validate_username(username):
            return "Invalid username. Username must be between 6 and 20 characters and contain only alphanumeric characters."
        if not self.validate_password(password):
            return "Invalid password. Password must be between 8 and 50 characters, contain at least one uppercase letter, one lowercase letter, and one number."
        if username in self.users:
            return "Username already exists."
        self.users[username] = password
        return "User registered successfully."

    def login(self, username, password):
        if username not in self.users or self.users[username] != password:
            return "Invalid username or password."
        if username in self.logged_in_users:
            return "User is already logged in."
        self.logged_in_users.append(username)
        return "User logged in successfully."

    def logout(self, username):
        if username not in self.logged_in_users:
            return "User is not logged in."
        self.logged_in_users.remove(username)
        return "User logged out successfully."

    def validate_username(self, username):
        if len(username) < 6 or len(username) > 20:
            return False
        if not re.match("^[A-Za-z0-9]+$", username):
            return False
        return True

    def validate_password(self, password):
        if len(password) < 8 or len(password) > 50:
            return False
        if not re.search("[a-z]", password):
            return False
        if not re.search("[A-Z]", password):
            return False
        if not re.search("[0-9]", password):
            return False
        return True

user_management = UserManagement()
print(user_management.register("user123", "Password1"))
print(user_management.login("user123", "Password1"))
print(user_management.logged_in_users)
print(user_management.logout("user123"))
print(user_management.logged_in_users)
print(user_management.users)