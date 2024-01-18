import random

def random_name_change(name):
    """Randomly changes one letter in a given name.

    Args:
        name: The name to be changed.

    Returns:
        A new string with one letter randomly changed.
    """

    random_index = random.randint(0, len(name) - 1)
    random_char = chr(random.randint(ord('a'), ord('z')))

    new_name = ""
    for i in range(len(name)):
        # Concatenate the random character at the random index, 
        # and the original character at all other indices
        new_name += random_char * (i == random_index) + name[i] * (i != random_index) 

    return new_name

# Example usage:
name = input('Enter a name: ')
new_name = random_name_change(name)
print('The new name is:', new_name)