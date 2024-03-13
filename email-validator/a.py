import re

def validate_email(email):
    # Check if the email is valid using regex
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False

    # Check if there's a number and a symbol present
    if not re.search(r"\d", email):
        return False
    if not re.search(r"[!@#$%^&*()-+?_=,<>/]", email):
        return False

    # Check if it is longer than 8 characters before the @ symbol and less than 30 total
    username = email.split('@')[0]
    if len(username) < 8 or len(email) > 30:
        return False

    # Check if the email doesn't contain any of these forbidden words
    forbidden_words = ['hot', 'dog', 'water', 'cat', 'trumpet', 'carbonated']
    for word in forbidden_words:
        if word in email:
            return False

    return True

# Test the function
print(validate_email("helloworld123@example.com"))  # Returns True
print(validate_email("hello@example.com"))  # Returns False, no number or symbol
print(validate_email("helloworld123@hot.com"))  # Returns False, contains forbidden word "hot"
print(validate_email("ho1!qwghet@example.com")) 