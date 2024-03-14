class Furniture:
    def __init__(self, name, condition, type, price):
        self.name = name
        self.condition = condition
        self.type = type
        self.price = price

class FurnitureStore:
    def __init__(self):
        self.inventory = []

    def add_furniture(self, furniture):
        self.inventory.append(furniture)
        print(f"{furniture.name} added to the inventory.")

    def sell_furniture(self, name):
        for furniture in self.inventory:
            if furniture.name == name:
                self.inventory.remove(furniture)
                print(f"{furniture.name} sold.")
                return
        print(f"{name} not found in inventory.")

    def buy_furniture(self, name, condition, type, price):
        new_furniture = Furniture(name, condition, type, price)
        self.inventory.append(new_furniture)
        print(f"{name} bought and added to the inventory.")

    def calculate_financing(self, name, down_payment):
        for furniture in self.inventory:
            if furniture.name == name:
                total = furniture.price
                financing = total - down_payment
                print(f"You need to finance ${financing} for {furniture.name}.")
                return
        print(f"{name} not found in inventory.")

# Demonstration
store = FurnitureStore()

# Adding furniture
store.add_furniture(Furniture("Sofa", "New", "Leather", 500))
store.add_furniture(Furniture("Table", "Used", "Wood", 200))

# Selling furniture
store.sell_furniture("Sofa")

# Buying furniture
store.buy_furniture("Bed", "New", "Steel", 300)

# Calculating financing
store.calculate_financing("Bed", 100)