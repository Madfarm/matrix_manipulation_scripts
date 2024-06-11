class Restaurant:
    def __init__(self, name):
        self.name = name
        self.dishes = {}

    def add_dish(self, name, ingredients, price):
        self.dishes[name] = {'ingredients': ingredients, 'price': price}

class Dish:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

class Ingredient:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def find_dishes(ingredients, restaurants):
    dishes = []
    for restaurant in restaurants:
        for dish_name, dish_info in restaurant.dishes.items():
            if all(ingredient in ingredients for ingredient in dish_info['ingredients']):
                dish_price = sum(ingredients[ingredient] for ingredient in dish_info['ingredients'])
                dishes.append({
                    'name': dish_name,
                    'restaurant': restaurant.name,
                    'restaurant_price': dish_info['price'],
                    'home_price': dish_price
                })
    return dishes

# Example usage:
restaurants = [
    Restaurant('Reel Seafood'),
    Restaurant('Century Tavern')
]

restaurants[0].add_dish('Fish and Chips', ['fish', 'chips'], 15.99)
restaurants[1].add_dish('Fish and Chips', ['fish', 'chips'], 12.99)

ingredients = {
    'fish': 5.99,
    'chips': 2.99
}

dishes = find_dishes(ingredients, restaurants)
for dish in dishes:
    print(f"Dish: {dish['name']}")
    print(f"Restaurant: {dish['restaurant']}")
    print(f"Restaurant Price: {dish['restaurant_price']}")
    print(f"Home Price: {dish['home_price']}")
    print()