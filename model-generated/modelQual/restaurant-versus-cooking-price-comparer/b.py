class Restaurant:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes

class Dish:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

class Ingredient:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def get_dishes(ingredients, restaurants):
    dishes = []
    for restaurant in restaurants:
        for dish in restaurant.dishes:
            if all(ingredient in ingredients for ingredient in dish.ingredients):
                dishes.append((dish.name, restaurant.name, dish.price, sum(ingredients[ingredient] for ingredient in dish.ingredients)))
    return dishes

# Example usage:
ingredients = {'chicken': 5, 'rice': 2, 'vegetables': 3, 'spices': 1}
restaurants = [
    Restaurant('Reel Seafood', [
        Dish('Chicken Fried Rice', ['chicken', 'rice', 'vegetables', 'spices'], 15),
        Dish('Grilled Chicken', ['chicken', 'vegetables', 'spices'], 12),
    ]),
    Restaurant('Century Tavern', [
        Dish('Chicken Fried Rice', ['chicken', 'rice', 'vegetables', 'spices'], 18),
        Dish('Grilled Chicken', ['chicken', 'vegetables', 'spices'], 15),
    ]),
]

dishes = get_dishes(ingredients, restaurants)
for dish in dishes:
    print(f'Dish: {dish[0]}, Restaurant: {dish[1]}, Price: {dish[2]}, Total Ingredient Price: {dish[3]}')