import random

class Pangolin:
    food_list = ['termite', 'ant', 'mealworm', 'grasshopper', 'cricket']

    def __init__(self, name, age, favorite_food, unique_id):
        self.name = name
        self.age = age
        self.favorite_food = favorite_food
        self.unique_id = unique_id

    def __repr__(self):
        return f'Pangolin({self.name}, {self.age}, {self.favorite_food}, {self.unique_id})'

def generate_pangolins(n):
    pangolins = []
    for i in range(n):
        name = f'Pangolin_{i+1}'
        age = random.randint(1, 20)
        favorite_food = random.choice(Pangolin.food_list)
        unique_id = i+1
        pangolin = Pangolin(name, age, favorite_food, unique_id)
        pangolins.append(pangolin)
    return pangolins

def calculate_total_food(pangolins):
    food_count = {}
    for pangolin in pangolins:
        if pangolin.favorite_food in food_count:
            food_count[pangolin.favorite_food] += 1
        else:
            food_count[pangolin.favorite_food] = 1
    return food_count

def sort_pangolins(pangolins):
    return sorted(pangolins, key=lambda pangolin: pangolin.age)

# Generate 10 pangolins
pangolins = generate_pangolins(10)

# Sort pangolins by age
pangolins = sort_pangolins(pangolins)

# Calculate total food required
total_food = calculate_total_food(pangolins)

# Print pangolins
for pangolin in pangolins:
    print(pangolin)

# Print total food required
for food, count in total_food.items():
    print(f'{food}: {count}')

