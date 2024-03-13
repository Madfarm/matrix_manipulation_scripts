class Bike:
    def __init__(self, name, original_price, condition="new"):
        self.name = name
        self.original_price = original_price
        self.current_price = original_price
        self.condition = condition

    def ride(self):
        if self.condition == "new":
            self.condition = "used"
        elif self.condition == "used":
            self.condition = "bad"
        else:
            self.condition = "very bad"
        self.calculate_price()

    def calculate_price(self):
        if self.condition == "new":
            self.current_price = self.original_price
        elif self.condition == "used":
            self.current_price = self.original_price * 0.8
        elif self.condition == "bad":
            self.current_price = self.original_price * 0.6
        else:
            self.current_price = self.original_price * 0.4

class BikeStore:
    def __init__(self):
        self.inventory = []
        self.total_value = 0
        self.money_earned = 0

    def calculate_total_value(self):
        self.total_value = sum([bike.current_price for bike in self.inventory])

    def test_drive(self):
        for bike in self.inventory:
            bike.ride()
        self.calculate_total_value()

    def add_bike(self, bike):
        self.inventory.append(bike)
        self.calculate_total_value()

    def sell_bike(self, bike):
        self.inventory.remove(bike)
        self.money_earned += bike.current_price

# Create bikes and store
bike1 = Bike("Mountain Bike", 1000)
bike2 = Bike("City Bike", 500)
store = BikeStore()

# Add bikes to store
store.add_bike(bike1)
store.add_bike(bike2)

print(bike1.current_price)
# Test drive all bikes in the store
store.test_drive()
print(bike1.current_price)

# Sell a bike
store.sell_bike(bike1)

# Print out final results
print("Final inventory:", [bike.name for bike in store.inventory])
print("Final total value:", store.total_value)
print("Final money earned:", store.money_earned)