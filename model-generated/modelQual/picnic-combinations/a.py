import itertools
import json

def generate_meals(snacks, drinks, sandwiches):
    # Validate input
    assert all(isinstance(snack, str) for snack in snacks), "Snacks must be a list of strings"
    assert all(isinstance(drink, str) for drink in drinks), "Drinks must be a list of strings"
    assert all(isinstance(sandwich, str) for sandwich in sandwiches), "Sandwiches must be a list of strings"

    # Generate all combinations
    meals = list(itertools.product(snacks, drinks, sandwiches))

    # Convert to JSON
    meals_json = json.dumps(meals)

    return meals_json

# Example usage
snacks = ["Chips", "Fruit", "Veggies"]
drinks = ["Soda", "Water", "Juice"]
sandwiches = ["Ham", "Turkey", "Veggie"]

meals_json = generate_meals(snacks, drinks, sandwiches)
print(meals_json)