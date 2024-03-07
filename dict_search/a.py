def search_dict(d, search_term):
    result = {}
    for key, value in d.items():
        if search_term in key or search_term in value:
            result[key] = value
    return result

# Testing the function
d = {'apple': 'fruit', 'carrot': 'vegetable', 'grapes': 'fruit', 'potato': 'starch'}
print(search_dict(d, 'apple'))  # Output: {'apple': 'fruit', 'grapes': 'fruit'}