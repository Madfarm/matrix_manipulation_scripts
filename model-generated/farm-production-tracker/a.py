from datetime import datetime, timedelta

class Animal:
    def __init__(self, id, name, type, arrival_date, food_consumption):
        self.id = id
        self.name = name
        self.type = type
        self.arrival_date = arrival_date
        self.food_consumption = food_consumption

    def calculate_food_needed(self, days):
        return self.food_consumption * days

    def produce_product(self):
        if self.type == 'chicken':
            return 'eggs', 10  # Assuming chickens lay 10 eggs per day
        elif self.type == 'cow' or self.type == 'goat':
            return 'milk', 5  # Assuming cows and goats produce 5 liters of milk per day
        elif self.type == 'pig':
            return 'truffles', 2  # Assuming pigs dig out 2 rare truffles per day

class Product:
    def __init__(self, type, quantity):
        self.type = type
        self.quantity = quantity

def calculate_total_food_needed(animals, days):
    total_food_needed = 0
    for animal in animals:
        total_food_needed += animal.calculate_food_needed(days)
    return total_food_needed

def report_total_yield(animals, days):
    total_yield = {}
    for animal in animals:
        product_type, product_quantity = animal.produce_product()
        if product_type in total_yield:
            total_yield[product_type] += product_quantity * days
        else:
            total_yield[product_type] = product_quantity * days
    return total_yield

# Example usage
goat1 = Animal(1, 'George', 'goat', datetime.now(), 10)
goat2 = Animal(2, 'Gracie', 'goat', datetime.now(), 12)
cow1 = Animal(3, 'Bessie', 'cow', datetime.now(), 8)
pig1 = Animal(4, 'Percy', 'pig', datetime.now(), 6)
chicken1 = Animal(5, 'Cluck', 'chicken', datetime.now(), 4)

animals = [goat1, goat2, cow1, pig1, chicken1]

days = 7

total_food_needed = calculate_total_food_needed(animals, days)
print(f'Total food needed in one week: {total_food_needed} kg')

total_yield = report_total_yield(animals, days)
print('Total yield of each product in one week:')
for product, quantity in total_yield.items():
    print(f'{product.capitalize()}: {quantity}')