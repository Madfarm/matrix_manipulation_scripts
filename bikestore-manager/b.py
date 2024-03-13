class Bike:
    def __init__(self, name, original_price, condition="good"):
        self.name = name
        self.original_price = original_price
        self.current_price = original_price
        self.condition = condition

    def ride(self):
        if self.condition == "good":
            self.condition = "bad"
        elif self.condition == "bad":
            self.condition = "very bad"
        self.calculate_price()

    def calculate_price(self):
        if self.condition == "good":
            self.current_price = self.original_price
        elif self.condition == "bad":
            self.current_price = self.original_price * 0.7
        elif self.condition == "very bad":
            self.current_price = self.original_price * 0.5

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
        self.calculate_total_value()

# Create bikes and store
bike1 = Bike("Mountain Bike", 1000)
bike2 = Bike("City Bike", 500)
store = BikeStore()

# Add bikes to store
store.add_bike(bike1)
store.add_bike(bike2)

# Perform test drive
store.test_drive()

# Sell a bike
store.sell_bike(bike1)

# Print out final results
print("Final inventory:", [bike.name for bike in store.inventory])
print("Final total value:", store.total_value)
print("Final money earned:", store.money_earned)