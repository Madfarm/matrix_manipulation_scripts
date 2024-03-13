import random

class Bee:
    def __init__(self, bee_type, job, energy, age):
        self.bee_type = bee_type
        self.job = job
        self.energy = energy
        self.age = age

    def work(self):
        if self.job == 'gatherer':
            self.energy -= 2
            return random.randint(1, 5)  # simulating gathering nectar/pollen
        elif self.job == 'caretaker':
            self.energy -= 1
            return random.randint(0, 2)  # simulating caring for young bees
        elif self.job == 'mate':
            self.energy -= 5
            return "Mated with the queen"
        elif self.job == 'lay egg':
            self.energy -= 3
            return "Laid an egg"

    def eat(self):
        self.energy += 5

    def age_increase(self):
        self.age += 1
        if self.age > 3:  # if bee's age is greater than 3, deplete energy faster
            self.energy -= 1

    def __str__(self):
        return f"Bee Type: {self.bee_type}, Job: {self.job}, Energy: {self.energy}, Age: {self.age}"

class Colony:
    def __init__(self, honey_production, honey_consumption):
        self.honey_production = honey_production
        self.honey_consumption = honey_consumption
        self.bees = []

    def add_bee(self, bee):
        self.bees.append(bee)

    def simulate_day(self):
        for bee in self.bees:
            if bee.energy <= 0:
                self.bees.remove(bee)
            else:
                result = bee.work()
                print(f"{bee} - {result}")
                bee.eat()
                bee.age_increase()

        self.honey_production += random.randint(0, 5)  # simulate honey production
        self.honey_consumption += random.randint(0, 2)  # simulate honey consumption

    def __str__(self):
        return f"Honey Production: {self.honey_production}, Honey Consumption: {self.honey_consumption}"

# Create a colony
colony = Colony(0, 0)

# Create bees
for _ in range(5):
    bee = Bee('worker', 'gatherer', 10, 0)
    colony.add_bee(bee)

for _ in range(3):
    bee = Bee('drone', 'mate', 15, 0)
    colony.add_bee(bee)

bee = Bee('queen', 'lay egg', 20, 0)
colony.add_bee(bee)

# Simulate a day
colony.simulate_day()

print(colony)