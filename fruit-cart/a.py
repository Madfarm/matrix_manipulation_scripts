class FruitCart:
    def __init__(self):
        self.fruits = {}
        self.balance = 0

    def add_fruit(self, name, quantity, price):
        self.fruits[name] = {"quantity": quantity, "price": price}

    def buy_fruit(self, name, quantity):
        if name in self.fruits and self.fruits[name]["quantity"] >= quantity:
            self.fruits[name]["quantity"] += quantity
            self.balance -= self.fruits[name]["price"] * quantity
            return f"Bought {quantity} {name} for {self.fruits[name]['price'] * quantity}."
        else:
            return f"Sorry, we don't have enough {name}."

    def sell_fruit(self, name, quantity):
        if name in self.fruits and self.fruits[name]["quantity"] >= quantity:
            self.fruits[name]["quantity"] -= quantity
            self.balance += self.fruits[name]["price"] * quantity
            return f"Sold {quantity} {name} for {self.fruits[name]['price'] * quantity}."
        else:
            return f"Sorry, we don't have enough {name}."

    def sort_by_name(self):
        sorted_fruits = sorted(self.fruits.items())
        return sorted_fruits

    def sort_by_price(self):
        sorted_fruits = sorted(self.fruits.items(), key=lambda x: x[1]['price'])
        return sorted_fruits

    def display_fruits(self):
        for name, fruit in self.fruits.items():
            print(f"{name}: {fruit['quantity']} left, ${fruit['price']} each")

    def display_balance(self):
        print(f"Balance: ${self.balance}")

# Example usage
cart = FruitCart()
cart.add_fruit("Apple", 10, 2.0)
cart.add_fruit("Banana", 15, 1.5)
cart.add_fruit("Cherry", 5, 3.0)

print("Initial menu:")
cart.display_fruits()

cart.buy_fruit("Apple", 3)
cart.buy_fruit("Banana", 2)
cart.sell_fruit("Cherry", 2)

print("\nMenu after buying and selling:")
cart.display_fruits()

print("\nSorted by name:")
sorted_fruits = cart.sort_by_name()
for name, fruit in sorted_fruits:
    print(f"{name}: {fruit['quantity']} left, ${fruit['price']} each")

print("\nSorted by price:")
sorted_fruits = cart.sort_by_price()
for name, fruit in sorted_fruits:
    print(f"{name}: {fruit['quantity']} left, ${fruit['price']} each")

cart.display_balance()