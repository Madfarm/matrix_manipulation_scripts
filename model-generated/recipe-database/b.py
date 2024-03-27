class Ingredient:
    def __init__(self, name, quantity, measurement_unit, calories_per_unit):
        self.name = name
        self.quantity = quantity
        self.measurement_unit = measurement_unit
        self.calories_per_unit = calories_per_unit

    def __str__(self):
        return f'{self.quantity} {self.measurement_unit} of {self.name}'


class Recipe:
    recipes_db = {}

    def __init__(self, id, name, ingredients, steps):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.recipes_db[id] = self

    def get_total_calories(self):
        total_calories = 0
        for ingredient in self.ingredients:
            total_calories += ingredient.calories_per_unit * ingredient.quantity
        return total_calories

    def __str__(self):
        return self.name

    @classmethod
    def search_recipe(cls, keyword):
        found_recipes = []
        for recipe in cls.recipes_db.values():
            if keyword in recipe.name or keyword in [ingredient.name for ingredient in recipe.ingredients]:
                found_recipes.append(recipe)
        return found_recipes


# Hardcoded data
rice = Ingredient('Rice', 2, 'cups', 120)
veg = Ingredient('Vegetables', 1, 'cup', 30)

recipe1 = Recipe(1, 'Vegetable Fried Rice', [rice, veg], ['Step 1: Boil water for rice', 'Step 2: Fried vegetables'])
recipe2 = Recipe(2, 'Tomato Rice', [rice, Ingredient('Tomato', 1, 'cup', 20)], ['Step 1: Boil water for rice', 'Step 2: Add tomatoes'])


# Demonstration
print("Search for 'Rice':")
for recipe in Recipe.search_recipe('Rice'):
    print(recipe)
    print(recipe.get_total_calories())
    print()

print("Search for 'Tomato':")
for recipe in Recipe.search_recipe('Tomato'):
    print(recipe)
    print(recipe.get_total_calories())
    print()

