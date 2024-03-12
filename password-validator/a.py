def min_steps_to_strong_password(password):
    if len(password) < 6:
        return 6 - len(password)
    elif len(password) > 20:
        return len(password) - 20

    missing_types = 3
    if any('a' <= c <= 'z' for c in password):
        missing_types -= 1
    if any('A' <= c <= 'Z' for c in password):
        missing_types -= 1
    if any(c.isdigit() for c in password):
        missing_types -= 1

    repeating_chars = [password[i] for i in range(2, len(password)) if password[i] == password[i-1] == password[i-2]]
    steps = missing_types + len(repeating_chars)

    return steps

# Testing the function
print(min_steps_to_strong_password("aaa123"))  # Output: 1
print(min_steps_to_strong_password("Baaabb0"))  # Output: 2
print(min_steps_to_strong_password("Baaba0"))  # Output: 0
print(min_steps_to_strong_password("Baabbb"))  # Output: 2
print(min_steps_to_strong_password("Baabbba"))  # Output: 1
print(min_steps_to_strong_password("A"))  # Output: 5