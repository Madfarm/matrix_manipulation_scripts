import random

class Pangolin:
    def __init__(self, name, age, food, id):
        self.name = name
        self.age = age
        self.food = food
        self.id = id

    def __repr__(self):
        return f'Pangolin({self.name}, {self.age}, {self.food}, {self.id})'

def calculate_food_total(pangolins):
    food_total = {}
    for pangolin in pangolins:
        if pangolin.food in food_total:
            food_total[pangolin.food] += 1
        else:
            food_total[pangolin.food] = 1
    return food_total

def sort_pangolins_by_age(pangolins):
    return sorted(pangolins, key=lambda pangolin: pangolin.age)

food_list = ['Termites', 'Ants', 'Mealworms', 'Grasshoppers', 'Crickets']

pangolins = [
    Pangolin('Pango', 5, random.choice(food_list), 1),
    Pangolin('Pangalina', 3, random.choice(food_list), 2),
    Pangolin('Pangobert', 7, random.choice(food_list), 3),
    Pangolin('Pangi', 2, random.choice(food_list), 4),
    Pangolin('Pangolette', 6, random.choice(food_list), 5),
]

sorted_pangolins = sort_pangolins_by_age(pangolins)
food_total = calculate_food_total(pangolins)

print('Sorted Pangolins:')
for pangolin in sorted_pangolins:
    print(pangolin)

print('\nFood Total:')
for food, total in food_total.items():
    print(f'{food}: {total}')