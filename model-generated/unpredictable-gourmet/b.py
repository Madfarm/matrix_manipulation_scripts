import random

# Define flavor profiles for each ingredient
ingredients = {
    'chicken': ['salty', 'umami'],
    'beef': ['salty', 'umami'],
    'pork': ['salty', 'umami'],
    'veal': ['salty', 'umami'],
    'lamb': ['salty', 'umami'],
    'fish': ['salty', 'umami'],
    'shrimp': ['salty', 'umami'],
    'bacon': ['salty', 'umami'],
    'ham': ['salty', 'umami'],
    'sausage': ['salty', 'umami'],
    'mushrooms': ['salty', 'umami'],
    'onions': ['sweet', 'umami'],
    'garlic': ['sweet', 'umami'],
    'bell peppers': ['sweet', 'umami'],
    'carrots': ['sweet', 'umami'],
    'potatoes': ['sweet', 'umami'],
    'squash': ['sweet', 'umami'],
    'corn': ['sweet', 'umami'],
    'tomatoes': ['sour', 'umami'],
    'lemon': ['sour', 'bitter'],
    'lime': ['sour', 'bitter'],
    'orange': ['sour', 'bitter'],
    'grapefruit': ['sour', 'bitter'],
    'vinegar': ['sour', 'umami'],
    'honey': ['sweet', 'umami'],
    'maple syrup': ['sweet', 'umami'],
    'balsamic glaze': ['sour', 'umami'],
    'soy sauce': ['salty', 'umami'],
    'teriyaki sauce': ['salty', 'umami'],
    'olive oil': ['umami'],
    'butter': ['umami'],
    'cream': ['umami'],
    'parmesan cheese': ['salty', 'umami'],
    'feta cheese': ['salty', 'umami'],
    'goat cheese': ['salty', 'umami'],
    'blue cheese': ['salty', 'umami'],
    'basil': ['sweet', 'umami'],
    'oregano': ['sweet', 'umami'],
    'thyme': ['sweet', 'umami'],
    'rosemary': ['sweet', 'umami'],
    'sage': ['sweet', 'umami'],
    'parsley': ['sweet', 'umami'],
    'chives': ['sweet', 'umami'],
}

# Function to generate a new recipe
def generate_recipe(num_ingredients=5):
    # Select random ingredients
    selected_ingredients = random.sample(list(ingredients.keys()), num_ingredients)
    
    # Determine the flavor profile of the recipe
    flavor_profile = set()
    for ingredient in selected_ingredients:
        flavor_profile.update(ingredients[ingredient])
    
    # Suggest a proportion for each ingredient
    proportions = {ingredient: random.randint(1, 5) for ingredient in selected_ingredients}
    
    # Generate a description of the recipe
    description = f"This recipe has a {' and '.join(flavor_profile)} flavor profile. "
    description += "The ingredients are: "
    for ingredient, proportion in proportions.items():
        description += f"{ingredient} ({proportion} parts), "
    description = description[:-2] + "."
    
    return description

# Generate and print a new recipe
print(generate_recipe())

