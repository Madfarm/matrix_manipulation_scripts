from datetime import datetime, timedelta

class Animal:
    def __init__(self, id, name, type, arrival_date, food_consumption):
        self.id = id
        self.name = name
        self.type = type
        self.arrival_date = datetime.strptime(arrival_date, '%Y-%m-%d')
        self.food_consumption = food_consumption

class Product:
    def __init__(self, type, production_frequency, production_quantity):
        self.type = type
        self.production_frequency = production_frequency
        self.production_quantity = production_quantity

class Farm:
    def __init__(self):
        self.animals = []
        self.products = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_product(self, product):
        self.products.append(product)

    def total_food_consumption(self, days):
        total_food = 0
        for animal in self.animals:
            total_food += animal.food_consumption * days
        return total_food

    def total_product_yield(self, days):
        total_yield = {}
        for product in self.products:
            if product.type == 'egg':
                total_yield[product.type] = len([animal for animal in self.animals if animal.type == 'chicken']) * product.production_quantity * (days / product.production_frequency)
            elif product.type == 'milk':
                total_yield[product.type] = len([animal for animal in self.animals if animal.type in ['cow', 'goat']]) * product.production_quantity * (days / product.production_frequency)
            elif product.type == 'truffle':
                total_yield[product.type] = len([animal for animal in self.animals if animal.type == 'pig']) * product.production_quantity * (days / product.production_frequency)
        return total_yield

farm = Farm()

farm.add_animal(Animal(1, 'Bessie', 'cow', '2022-01-01', 10))
farm.add_animal(Animal(2, 'Gary', 'goat', '2022-01-01', 5))
farm.add_animal(Animal(3, 'Cluck', 'chicken', '2022-01-01', 2))
farm.add_animal(Animal(4, 'Porky', 'pig', '2022-01-01', 8))

farm.add_product(Product('milk', 2, 10))
farm.add_product(Product('egg', 1, 12))
farm.add_product(Product('truffle', 10, 1))

print("Total food needed in one week: ", farm.total_food_consumption(7))
print("Total yield of each product in one week: ", farm.total_product_yield(7))