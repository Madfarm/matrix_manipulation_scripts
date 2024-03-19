class Customer:
    def __init__(self, customer_id, name, rides_ridden=0, foods_eaten=0, rewards_balance=0):
        self.customer_id = customer_id
        self.name = name
        self.rides_ridden = rides_ridden
        self.foods_eaten = foods_eaten
        self.rewards_balance = rewards_balance

    def ride_ride(self):
        self.rides_ridden += 1
        self.rewards_balance -= 10

    def eat_food(self):
        self.foods_eaten += 1
        self.rewards_balance += 10

        if self.rewards_balance > 200:
            print(f"Congratulations, {self.name}! Your rewards balance has reached 200 or more!")

    def get_customer_details(self):
        return {
            "Customer ID": self.customer_id,
            "Name": self.name,
            "Rides Ridden": self.rides_ridden,
            "Foods Eaten": self.foods_eaten,
            "Rewards Balance": self.rewards_balance
        }


# Demonstration
customer1 = Customer(1, "John Doe")
customer1.ride_ride()
customer1.ride_ride()
customer1.eat_food()
customer1.eat_food()

print(customer1.get_customer_details())