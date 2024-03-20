class Ingredient:
    def __init__(self, name, type, cooking_method):
        self.name = name
        self.type = type
        self.cooking_method = cooking_method

class Spice:
    def __init__(self, name, interaction):
        self.name = name
        self.interaction = interaction

class Recipe:
    def __init__(self, name, ingredients, spices):
        self.name = name
        self.ingredients = ingredients
        self.spices = spices

    def modify_recipe(self, modifications):
        for modification in modifications:
            if modification['type'] == 'exclude':
                self.ingredients = [i for i in self.ingredients if i.type != modification['value']]
            elif modification['type'] == 'adjust_heat':
                for spice in self.spices:
                    if spice.name == modification['value']:
                        spice.interaction = modification['new_level']

    def print_recipe(self):
        print(f"Recipe: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"{ingredient.name} - {ingredient.type}, cooked by {ingredient.cooking_method}")
        print("Spices:")
        for spice in self.spices:
            print(f"{spice.name} - {spice.interaction}")

# Create ingredients
ingredient1 = Ingredient('Chicken', 'meat', 'grilled')
ingredient2 = Ingredient('Carrot', 'vegetable', 'steamed')
ingredient3 = Ingredient('Rice', 'grain', 'cooked')
ingredient4 = Ingredient('Milk', 'dairy', 'heated')

# Create spices
spice1 = Spice('Pepper', 'hot')
spice2 = Spice('Garlic', 'mild')

# Create a recipe
recipe = Recipe('Chicken and Rice', [ingredient1, ingredient2, ingredient3, ingredient4], [spice1, spice2])

# Print original recipe
recipe.print_recipe()

# Modify recipe
recipe.modify_recipe([{'type': 'exclude', 'value': 'dairy'}, {'type': 'adjust_heat', 'value': 'Pepper', 'new_level': 'very hot'}])

# Print modified recipe
recipe.print_recipe()