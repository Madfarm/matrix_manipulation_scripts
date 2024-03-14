class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.logged_in = False
        self.login_count = 0

class UserSystem:
    def __init__(self):
        self.users = {}
        self.logged_in_users = set()

    def validate_username(self, username):
        if len(username) < 3:
            return False
        if not username.isalnum():
            return False
        return True

    def validate_password(self, password):
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isalpha() for char in password):
            return False
        return True

    def register_user(self, username, password):
        if not self.validate_username(username):
            print("Invalid username")
            return
        if not self.validate_password(password):
            print("Invalid password")
            return
        if username in self.users:
            print("Username already exists")
            return
        self.users[username] = User(username, password)
        print("User registered successfully")

    def login_user(self, username, password):
        if username not in self.users or self.users[username].password != password:
            print("Invalid username or password")
            return
        if self.users[username].logged_in:
            print("User is already logged in")
            return
        self.users[username].logged_in = True
        self.users[username].login_count += 1
        self.logged_in_users.add(username)
        print("User logged in successfully")

    def logout_user(self, username):
        if username not in self.users or not self.users[username].logged_in:
            print("User is not logged in")
            return
        self.users[username].logged_in = False
        self.logged_in_users.remove(username)
        print("User logged out successfully")

    def logout_all_users(self):
        for username in list(self.logged_in_users):
            self.logout_user(username)

# Testing the new functionality
user_system = UserSystem()
user_system.register_user('user1', 'password1')
user_system.register_user('user2', 'password2')

user_system.login_user('user1', 'password1')
user_system.login_user('user2', 'password2')
user_system.login_user('user1', 'password1')

print(user_system.users['user1'].login_count)  # prints: 2
print(user_system.users['user2'].login_count)  # prints: 1

user_system.logout_all_users()
print(user_system.logged_in_users)  # prints: set()