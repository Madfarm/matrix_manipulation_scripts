class FruitCart:
    def __init__(self):
        self.fruits = {}
        self.money = 0

    def add_fruit(self, name, quantity, price):
        if name in self.fruits:
            self.fruits[name]['quantity'] += quantity
        else:
            self.fruits[name] = {'quantity': quantity, 'price': price}

    def buy_fruit(self, name, quantity):
        if name in self.fruits and self.fruits[name]['quantity'] >= quantity:
            self.fruits[name]['quantity'] -= quantity
            self.money += quantity * self.fruits[name]['price']
        else:
            print("Not enough fruit in stock")

    def display_fruit(self):
        print("Fruit Cart Menu:")
        for fruit, details in self.fruits.items():
            print(f"{fruit}: {details['quantity']} left, ${details['price']} each")
        print(f"Total money: ${self.money}")

    def sort_fruit_by_name(self):
        sorted_fruits = sorted(self.fruits.items())
        for fruit, details in sorted_fruits:
            print(f"{fruit}: {details['quantity']} left, ${details['price']} each")

    def sort_fruit_by_price(self):
        sorted_fruits = sorted(self.fruits.items(), key=lambda x: x[1]['price'])
        for fruit, details in sorted_fruits:
            print(f"{fruit}: {details['quantity']} left, ${details['price']} each")

# Testing the FruitCart class
cart = FruitCart()
cart.add_fruit("Apple", 10, 2.00)
cart.add_fruit("Banana", 5, 1.50)
cart.add_fruit("Cherry", 7, 3.00)

cart.display_fruit()

cart.buy_fruit("Apple", 3)
cart.buy_fruit("Banana", 2)

cart.display_fruit()

cart.sort_fruit_by_name()
cart.sort_fruit_by_price()