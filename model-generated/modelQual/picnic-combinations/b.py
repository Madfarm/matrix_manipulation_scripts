import itertools
import json

def generate_meals(snacks, drinks, sandwiches):
    # Validate input
    assert isinstance(snacks, list), "Snacks must be a list"
    assert isinstance(drinks, list), "Drinks must be a list"
    assert isinstance(sandwiches, list), "Sandwiches must be a list"
    
    # Generate all possible combinations
    meals = list(itertools.product(snacks, drinks, sandwiches))
    
    # Convert each meal to a list
    meals = [list(meal) for meal in meals]
    
    # Convert the list of meals to JSON
    meals_json = json.dumps(meals)
    
    return meals_json

# Example usage
snacks = ['chips', 'cookies', 'fruit']
drinks = ['soda', 'water', 'juice']
sandwiches = ['ham and cheese', 'turkey', 'veggie']

meals_json = generate_meals(snacks, drinks, sandwiches)
print(meals_json)