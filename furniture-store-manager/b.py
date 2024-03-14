class Furniture:
    def __init__(self, name, condition, type, price):
        self.name = name
        self.condition = condition
        self.type = type
        self.price = price

class Store:
    def __init__(self):
        self.inventory = []

    def add_furniture(self, furniture):
        self.inventory.append(furniture)

    def sell_furniture(self, name):
        for furniture in self.inventory:
            if furniture.name == name:
                self.inventory.remove(furniture)
                return furniture
        return None

    def buy_furniture(self, furniture):
        self.inventory.append(furniture)

    def calculate_financing(self, price, time_period=12):
        # Assuming a simple interest rate of 5%
        interest_rate = 0.05
        return price * (1 + interest_rate / 12) ** time_period

# Creating a new store
store = Store()

# Adding furniture to the store
store.add_furniture(Furniture("Sofa", "New", "Leather", 500))
store.add_furniture(Furniture("Table", "Used", "Wood", 200))

# Selling furniture
sold_furniture = store.sell_furniture("Sofa")
if sold_furniture:
    print(f"Sold a {sold_furniture.name} for ${sold_furniture.price}")
else:
    print("Furniture not available")

# Buying furniture
new_furniture = Furniture("Chair", "New", "Metal", 100)
store.buy_furniture(new_furniture)

# Calculating financing for a furniture
price = 500
financing_amount = store.calculate_financing(price)
print(f"Financing for a ${price} furniture over 12 months is ${financing_amount}")