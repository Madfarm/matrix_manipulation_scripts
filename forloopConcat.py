import random

def random_name_change(name):
    """Randomly changes one letter in a given name.

    Args:
      name: The name to be changed.

    Returns:
      A new string with one letter randomly changed.
    """

    # Generate a random index within the range of the string length.
    random_index = random.randint(0, len(name) - 1)

    # Generate a random replacement character.
    random_character = chr(random.randint(ord('a'), ord('z')))

    # Replace the character at the random index with the random character.
    new_name = name[:random_index] + random_character + name[random_index + 1:]

    return new_name

# Example usage:
name = input('Enter a name: ')
new_name = random_name_change(name)
print('The new name is:', new_name)