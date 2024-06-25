def vape_recommender(flavor, nicotine=None, sort=False):
    vapes = [
        {"flavor": ("apple", "geek bar apple"), "nicotine": 3},
        {"flavor": ("watermelon", "geek bar watermelon"), "nicotine": 5},
        {"flavor": ("strawberry", "geek bar strawberry"), "nicotine": 3},
        {"flavor": ("blue raspberry", "geek bar blue raspberry"), "nicotine": 5},
        {"flavor": ("white gummy ice", "geek bar white gummy ice"), "nicotine": 3},
        {"flavor": ("crazy melon", "geek bar crazy melon"), "nicotine": 5},
    ]

    if sort:
        matching_entries = [
            vape for vape in vapes 
            if (flavor in vape["flavor"] and (nicotine is None or vape["nicotine"] == nicotine))
        ]
        non_matching_entries = [
            vape for vape in vapes 
            if (flavor not in vape["flavor"] or (nicotine is not None and vape["nicotine"] != nicotine))
        ]
        return matching_entries + non_matching_entries
    
    if nicotine is not None:
        vapes = [vape for vape in vapes if vape["nicotine"] == nicotine]

    if flavor:
        vapes = [vape for vape in vapes if flavor in vape["flavor"]]

    return vapes

# Example usage:
print(vape_recommender("apple"))  # Returns all vapes with "apple" in the flavor
print(vape_recommender("apple", 3))  # Returns all vapes with "apple" in the flavor and nicotine level 3
print(vape_recommender("apple", 3, True))  # Returns all vapes with any matching criteria pushed to the top