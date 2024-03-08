def create_string_from_dict(char_dict):
    result_string = ''
    for char, count in char_dict.items():
        result_string += char * count
    return result_string

# Testing the function
char_dict = {'a': 3, 'b': 2, 'c': 1}
print(create_string_from_dict(char_dict))  # Output: 'aaabbc'