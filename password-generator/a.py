import string
import random

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print("Password length should be at least 8")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

# Generate a password of length 12
print(generate_password(12))