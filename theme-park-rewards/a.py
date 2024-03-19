class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.total_rides_ridden = 0
        self.total_foods_eaten = 0
        self.rewards_balance = 0

    def ride_ride(self):
        self.total_rides_ridden += 1
        self.rewards_balance -= 20
        print(f"{self.name} has ridden a ride. Their new rewards balance is {self.rewards_balance}.")

    def eat_food(self):
        self.total_foods_eaten += 1
        self.rewards_balance += 10
        print(f"{self.name} has eaten food. Their new rewards balance is {self.rewards_balance}.")
        if self.rewards_balance > 200:
            print(f"Congratulations, {self.name}! Your rewards balance has exceeded 200!")

# Demonstration
customer1 = Customer(1, "John")
customer1.ride_ride()
customer1.eat_food()
customer1.ride_ride()
customer1.eat_food()
customer1.eat_food()