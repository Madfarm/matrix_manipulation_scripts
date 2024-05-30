class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def can_make(self, available_ingredients):
        return all(ingredient in available_ingredients for ingredient in self.ingredients)

class RecipeBook:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, name, ingredients):
        self.recipes.append(Recipe(name, ingredients))

    def get_recipes(self, ingredients):
        return [recipe.name for recipe in self.recipes if recipe.can_make(ingredients)]

# Test the classes
recipe_book = RecipeBook()
recipe_book.add_recipe('Cantina Chicken Tacos', ['slow-roasted chicken', 'signature pico de gallo', 'fresh purple cabbage', 'crispy white corn shell', 'flavorful avocado verde salsa'])
recipe_book.add_recipe('Cheesy Chicken Empanada', ['crispy pastry dough', 'seasoned shredded chicken', 'melted three-cheese blend', 'Spicy Ranch dipping sauce'])

available_ingredients = ['slow-roasted chicken', 'signature pico de gallo', 'fresh purple cabbage', 'crispy white corn shell', 'flavorful avocado verde salsa', 'crispy pastry dough', 'seasoned shredded chicken', 'melted three-cheese blend', 'Spicy Ranch dipping sauce']

print(recipe_book.get_recipes(available_ingredients))