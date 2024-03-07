def search_dict(dictionary, search_term):
    # Iterate over each key-value pair in the dictionary
    for key, value in dictionary.items():
        # Check if the search term matches the key or value
        if search_term == key or search_term == value:
            return True  # Return True if a match is found
    return False  # Return False if no match is found

# Example usage
my_dict = {"apple": "fruit", "carrot": "vegetable", "grapes": "fruit"}
print(search_dict(my_dict, "apple"))  # Output: True
print(search_dict(my_dict, "fruit"))  # Output: False