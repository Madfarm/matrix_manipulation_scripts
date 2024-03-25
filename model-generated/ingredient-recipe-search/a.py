class Recipe:
    def __init__(self, name, ingredients, preparation, cook_time, servings, region):
        self.name = name
        self.ingredients = ingredients
        self.preparation = preparation
        self.cook_time = cook_time
        self.servings = servings
        self.region = region

recipes = [
    Recipe('Chicken Tikka Masala', ['chicken', 'tomato sauce', 'onion', 'garam masala', 'yogurt', 'lemon juice', 'heavy cream', 'butter'], 'In a blender, combine yogurt, lemon juice, garam masala, and 1/2 teaspoon cumin powder. Add the mixture to the chicken and marinate for at least 30 minutes. Heat oil in a pan and cook the onion until translucent. Add the chicken and cook until browned. Add the tomato sauce, heavy cream, and butter. Simmer for 15 minutes.', '30 minutes', 4, 'Indian'),
    Recipe('Grilled Chicken Salad', ['chicken', 'lettuce', 'tomato', 'avocado', 'cheese', 'bacon'], 'In a bowl, combine chicken, lettuce, tomato, avocado, and cheese. Grill the bacon until crispy. Add the bacon to the salad.', '10 minutes', 2, 'American'),
    Recipe('Spaghetti Bolognese', ['spaghetti', 'ground beef', 'onion', 'carrot', 'celery', 'tomato sauce', 'red wine', 'beef broth', 'parmesan cheese'], 'Cook the spaghetti according to package instructions. In a pan, cook the ground beef until browned. Add the onion, carrot, and celery and cook until the vegetables are tender. Add the tomato sauce, red wine, and beef broth. Simmer for 15 minutes. Combine the spaghetti and meat sauce. Sprinkle with parmesan cheese.', '45 minutes', 4, 'Italian'),
    Recipe('French Toast', ['bread', 'eggs', 'milk', 'cinnamon', 'sugar'], 'In a shallow dish, whisk together eggs, milk, cinnamon, and sugar. Dip the bread slices in the mixture and cook in a skillet until golden brown.', '15 minutes', 2, 'French'),
    Recipe('Baked Salmon', ['salmon', 'lemon juice', 'olive oil', 'salt', 'pepper'], 'Preheat oven to 400°F (200°C). Season the salmon with salt and pepper. In a bowl, mix together lemon juice and olive oil. Brush the mixture onto the salmon and bake for 12-15 minutes or until cooked through.', '20 minutes', 4, 'American'),
]

def find_recipes(ingredients):
    possible_recipes = []
    for recipe in recipes:
        if all(ingredient in ingredients for ingredient in recipe.ingredients):
            possible_recipes.append(recipe)
    return possible_recipes

def suggest_recipe(ingredients):
    possible_recipes = find_recipes(ingredients)
    if possible_recipes:
        return possible_recipes[0]
    else:
        leftover_ingredients = [ingredient for ingredient in ingredients if not any(ingredient in recipe.ingredients for recipe in recipes)]
        additional_ingredients = [ingredient for recipe in recipes for ingredient in recipe.ingredients if not any(ingredient in ingredients for ingredient in recipe.ingredients)]
        return f'Leftover ingredients: {leftover_ingredients}, Additional ingredients needed: {additional_ingredients}'

# Test the program
ingredients = ['tomato sauce', 'onion', 'garam masala', 'yogurt', 'lemon juice', 'heavy cream', 'butter', 'cinnamon']
recipe = suggest_recipe(ingredients)
print(f'Recipe: {recipe.name}')
print(f'Ingredients: {recipe.ingredients}')
print(f'Preparation: {recipe.preparation}')
print(f'Cook time: {recipe.cook_time}')
print(f'Servings: {recipe.servings}')
print(f'Culinary region: {recipe.region}')