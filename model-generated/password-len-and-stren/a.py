import random
import string


def generate_password(length, min_strength):
    assert length > 0, "Length must be a positive integer"
    assert min_strength in ["weak", "medium", "strong"], "Invalid strength level"


    if min_strength == "weak":
        chars = string.ascii_lowercase
    elif min_strength == "medium":
        if random.choice([True, False]):
            chars = string.ascii_letters
        else:
            chars = string.ascii_lowercase + string.digits
    elif min_strength == "strong":
        chars = string.ascii_letters + string.digits + string.punctuation


    password = ''.join(random.choice(chars) for _ in range(length))


    # Validate the generated password
    if min_strength == "weak":
        assert all(c.islower() for c in password), "Weak password should only contain lowercase letters"
    elif min_strength == "medium":
        assert any(c.isupper() for c in password) or any(c.isdigit() for c in password), "Medium password should contain at least one uppercase letter or digit"
    elif min_strength == "strong":
        assert (any(c.isupper() for c in password) and any(c.isdigit() for c in password) and 
                any(c in string.punctuation for c in password)), "Strong password should contain at least one uppercase letter, digit, and special character"


    return password


length = 12
min_strength = "medium"
generate_password(length, min_strength)