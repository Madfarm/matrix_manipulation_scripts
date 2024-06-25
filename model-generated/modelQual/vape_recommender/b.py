def vape_recommender(flavor, nicotine=None, sort=False):
    vapes = [
        {"flavor": "apple", "nicotine": 3},
        {"flavor": "banana", "nicotine": 6},
        {"flavor": "cherry", "nicotine": 3},
        {"flavor": "date", "nicotine": 6},
        {"flavor": "elderberry", "nicotine": 3},
        {"flavor": "fig", "nicotine": 6},
        {"flavor": "grape", "nicotine": 3},
        {"flavor": "honeydew", "nicotine": 6},
        # Add more vapes here...
    ]

    if nicotine is not None:
        vapes = [vape for vape in vapes if vape["nicotine"] == nicotine]

    if flavor:
        vapes = [vape for vape in vapes if vape["flavor"] == flavor]

    if sort:
        vapes.sort(key=lambda x: (x["flavor"] == flavor, x["nicotine"] == nicotine), reverse=True)

    return vapes

# Test the function
print(vape_recommender("apple"))  # Returns all vapes with "apple" flavor
print(vape_recommender("apple", 3))  # Returns all vapes with "apple" flavor and 3mg nicotine
print(vape_recommender("apple", 3, True))  # Returns all vapes with "apple" flavor and 3mg nicotine, sorted by matching flavor and nicotine
