class Ingredient:
    def __init__(self, name, ingredient_type, cooking_method):
        self.name = name
        self.ingredient_type = ingredient_type
        self.cooking_method = cooking_method

    def __str__(self):
        return f"{self.name} ({self.ingredient_type}, {self.cooking_method})"


class Spice:
    def __init__(self, name, interactions):
        self.name = name
        self.interactions = interactions

    def __str__(self):
        return f"{self.name} (interacts with {', '.join(self.interactions)})"


class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.spices = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def add_spice(self, spice):
        self.spices.append(spice)

    def remove_ingredient(self, ingredient_name):
        self.ingredients = [ingredient for ingredient in self.ingredients if ingredient.name != ingredient_name]

    def remove_spice(self, spice_name):
        self.spices = [spice for spice in self.spices if spice.name != spice_name]

    def __str__(self):
        ingredients_str = '\n'.join([str(ingredient) for ingredient in self.ingredients])
        spices_str = '\n'.join([str(spice) for spice in self.spices])
        return f"{self.name}\nIngredients:\n{ingredients_str}\nSpices:\n{spices_str}"


# Demonstration
chicken = Ingredient("Chicken", "meat", "grilled")
carrots = Ingredient("Carrots", "vegetable", "steamed")
rice = Ingredient("Rice", "grain", "cooked")
cheese = Ingredient("Cheese", "dairy", "grated")
garlic = Spice("Garlic", ["Chicken", "Carrots"])
oregano = Spice("Oregano", ["Chicken", "Rice"])
parmesan = Spice("Parmesan", ["Cheese"])

recipe = Recipe("Chicken and Rice")
recipe.add_ingredient(chicken)
recipe.add_ingredient(carrots)
recipe.add_ingredient(rice)
recipe.add_ingredient(cheese)
recipe.add_spice(garlic)
recipe.add_spice(oregano)
recipe.add_spice(parmesan)

print(recipe)

# User can modify the recipe
recipe.remove_ingredient("Cheese")
recipe.remove_spice("Parmesan")

print(recipe)