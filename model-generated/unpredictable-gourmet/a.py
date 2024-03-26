import random

# Define flavor profiles for ingredients
ingredients = {
    'chicken': ['salty', 'umami'],
    'beef': ['salty', 'umami'],
    'pork': ['salty', 'umami'],
    'veal': ['salty', 'umami'],
    'lamb': ['salty', 'umami'],
    'fish': ['salty', 'umami'],
    'shrimp': ['salty', 'umami'],
    'lobster': ['salty', 'umami'],
    'crab': ['salty', 'umami'],
    'bacon': ['salty', 'umami'],
    'ham': ['salty', 'umami'],
    'sausage': ['salty', 'umami'],
    'mushroom': ['umami'],
    'onion': ['sweet', 'umami'],
    'garlic': ['sweet', 'umami'],
    'bell pepper': ['sweet', 'umami'],
    'carrot': ['sweet', 'umami'],
    'potato': ['sweet', 'umami'],
    'squash': ['sweet', 'umami'],
    'corn': ['sweet', 'umami'],
    'apple': ['sweet', 'sour'],
    'pear': ['sweet', 'sour'],
    'peach': ['sweet', 'sour'],
    'plum': ['sweet', 'sour'],
    'pineapple': ['sweet', 'sour'],
    'lemon': ['sour'],
    'lime': ['sour'],
    'orange': ['sour'],
    'grapefruit': ['sour'],
    'watermelon': ['sour'],
    'grapes': ['sweet', 'sour'],
    'strawberry': ['sweet', 'sour'],
    'raspberry': ['sweet', 'sour'],
    'blueberry': ['sweet', 'sour'],
    'blackberry': ['sweet', 'sour'],
    'kiwi': ['sweet', 'sour'],
    'banana': ['sweet'],
    'mango': ['sweet'],
    'pecan': ['sweet', 'umami'],
    'walnut': ['sweet', 'umami'],
    'almond': ['sweet', 'umami'],
    'butter': ['sweet', 'umami'],
    'cream': ['sweet', 'umami'],
    'cheese': ['sweet', 'umami'],
    'bread': ['sweet', 'umami'],
    'rice': ['sweet', 'umami'],
    'pasta': ['sweet', 'umami'],
    'tomato': ['sour', 'umami'],
    'egg': ['salty', 'umami'],
    'soy sauce': ['salty', 'umami'],
    'olive oil': ['salty', 'umami'],
    'vinegar': ['sour', 'umami'],
    'wine': ['sweet', 'sour', 'umami'],
    'beer': ['sweet', 'sour', 'umami'],
}

# Generate a new recipe
def generate_recipe():
    # Select a random main ingredient
    main_ingredient = random.choice(list(ingredients.keys()))

    # Select a random flavor profile for the main ingredient
    main_flavor = random.choice(ingredients[main_ingredient])

    # Select a random ingredient that complements the main flavor
    complementary_ingredient = random.choice([i for i, f in ingredients.items() if main_flavor in f])

    # Suggest a proportion for each ingredient
    main_proportion = random.uniform(0.25, 0.75)
    complementary_proportion = 1 - main_proportion

    # Generate a description of the recipe
    description = f"This recipe features {main_ingredient} as the main ingredient, complemented by {complementary_ingredient}. The proportion of {main_ingredient} is {main_proportion} cups, while {complementary_ingredient} makes up {complementary_proportion} cups."

    return description

# Print a new recipe
print(generate_recipe())