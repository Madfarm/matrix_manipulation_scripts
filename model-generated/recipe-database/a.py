class Ingredient:
    def __init__(self, name, quantity, measurement_unit, calories_per_unit):
        self.name = name
        self.quantity = quantity
        self.measurement_unit = measurement_unit
        self.calories_per_unit = calories_per_unit

class Recipe:
    def __init__(self, id, name, ingredients, steps):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.steps = steps

    def calculate_calories(self):
        total_calories = 0
        for ingredient in self.ingredients:
            total_calories += ingredient.quantity * ingredient.calories_per_unit
        return total_calories

class RecipeDatabase:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def search_by_name(self, name):
        return [recipe for recipe in self.recipes if recipe.name == name]

    def search_by_ingredient(self, ingredient_name):
        return [recipe for recipe in self.recipes if any(ingredient.name == ingredient_name for ingredient in recipe.ingredients)]

# Hardcoded data
ingredient1 = Ingredient('Flour', 2, 'cups', 400)
ingredient2 = Ingredient('Eggs', 3, 'large', 70)
recipe1 = Recipe(1, 'Pancakes', [ingredient1, ingredient2], ['Mix ingredients', 'Cook on stovetop'])

ingredient3 = Ingredient('Chicken', 1.5, 'kilograms', 200)
ingredient4 = Ingredient('Rice', 2, 'cups', 250)
recipe2 = Recipe(2, 'Chicken Fried Rice', [ingredient3, ingredient4], ['Cook chicken', 'Cook rice', 'Mix together'])

# Create database and add recipes
database = RecipeDatabase()
database.add_recipe(recipe1)
database.add_recipe(recipe2)

# Search for recipes
print(database.search_by_name('Pancakes'))
print(database.search_by_ingredient('Eggs'))

# Calculate calories
print(recipe1.calculate_calories())
print(recipe2.calculate_calories())