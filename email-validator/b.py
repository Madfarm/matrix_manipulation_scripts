import re

def validate_email(email):
    # check if the string is a valid email using regex
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False

    # check if there's a number and a symbol present
    if not re.search(r"\d", email) or not re.search(r"[^\w\s]", email):
        return False

    # check if it is longer than 8 characters before the @ symbol and less than 30 total
    local_part, domain = email.split("@")
    if len(local_part) < 8 or len(email) > 30:
        return False

    # check if the email doesn't contain any of these forbidden words
    forbidden_words = ["hot", "dog", "water", "cat", "trumpet", "carbonated"]
    for word in forbidden_words:
        if word in email:
            return False

    # if the email passes all of the checks
    return True

# test the function
print(validate_email("test.email+123@example.com"))  # True
print(validate_email("test.email@example.com"))  # False
print(validate_email("test.email123@example.com"))  # False
print(validate_email("test.email+123@example.com"))  # True
print(validate_email("ho1!qwghet@example.com"))  # False
print(validate_email("test.email+123@trumpet.com"))  # False