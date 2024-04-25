import random
import string


def generate_password(length, min_strength):
    if min_strength == "weak":
        characters = string.ascii_lowercase
    elif min_strength == "medium":
        characters = string.ascii_letters + string.digits
    elif min_strength == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid strength level")


    password = ''.join(random.choice(characters) for _ in range(length))
    return password


length = 12
min_strength = "medium"
print(generate_password(length, min_strength))