class Recipe:
    def __init__(self, name, ingredients, preparation, cook_time, servings, region):
        self.name = name
        self.ingredients = ingredients
        self.preparation = preparation
        self.cook_time = cook_time
        self.servings = servings
        self.region = region

# Hardcoded recipes
recipes = [
    Recipe('Pasta Carbonara', ['pasta', 'eggs', 'parmesan cheese', 'pancetta'], 'Cook pasta, scramble eggs and mix with parmesan cheese and pancetta.', '20 minutes', 4, 'Italian'),
    Recipe('Chicken Tikka Masala', ['chicken breast', 'lemon juice', 'yogurt', 'garam masala', 'onion', 'tomato', 'cumin', 'cayenne pepper'], 'Marinate chicken in lemon juice and yogurt, then grill or bake. Make the sauce with onion, tomato, cumin, cayenne pepper and garam masala and serve with rice.', '30 minutes', 4, 'Indian'),
    Recipe('Grilled Cheese Sandwich', ['bread', 'cheese', 'butter'], 'Butter bread, place cheese between two slices and grill until melted.', '5 minutes', 2, 'American'),
    # Add more recipes here...
]

def find_recipes(ingredients):
    possible_recipes = []
    for recipe in recipes:
        if all(ingredient in ingredients for ingredient in recipe.ingredients):
            possible_recipes.append(recipe)
    return possible_recipes

def suggest_additional_recipes(ingredients):
    additional_recipes = []
    for recipe in recipes:
        if any(ingredient in recipe.ingredients for ingredient in ingredients):
            additional_recipes.append(recipe)
    return additional_recipes

def suggest_additional_ingredients(ingredients):
    all_ingredients = [ingredient for recipe in recipes for ingredient in recipe.ingredients]
    suggested_ingredients = list(set(all_ingredients) - set(ingredients))
    return suggested_ingredients

# Test the program
my_ingredients = ['pasta', 'eggs', 'parmesan cheese', 'pancetta', 'chicken breast', 'lemon juice', 'yogurt', 'garam masala', 'onion', 'tomato', 'cumin', 'cayenne pepper']
possible_recipes = find_recipes(my_ingredients)
additional_recipes = suggest_additional_recipes(my_ingredients)
additional_ingredients = suggest_additional_ingredients(my_ingredients)

print("Possible recipes:")
for recipe in possible_recipes:
    print(recipe.name)

print("\nAdditional recipes using your ingredients:")
for recipe in additional_recipes:
    print(recipe.name)

print("\nSuggested additional ingredients:")
for ingredient in additional_ingredients:
    print(ingredient)