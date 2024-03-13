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
            return random.randint(1, 3)  # simulating caring for young bees
        elif self.job == 'mate':
            self.energy -= 5
            return "Mated with the queen"
        elif self.job == 'lay egg':
            self.energy -= 3
            return "Laid an egg"

    def eat(self):
        self.energy += 5
        return f"Bee is now at {self.energy} energy"

    def get_info(self):
        return f"Type: {self.bee_type}, Job: {self.job}, Energy: {self.energy}, Age: {self.age}"


class Colony:
    def __init__(self, honey):
        self.honey = honey
        self.bees = []

    def add_bee(self, bee):
        self.bees.append(bee)

    def consume_honey(self, amount):
        self.honey -= amount
        return f"Colony consumed {amount} honey, remaining: {self.honey}"

    def produce_honey(self, amount):
        self.honey += amount
        return f"Colony produced {amount} honey, total: {self.honey}"

    def simulate_day(self):
        for bee in self.bees:
            if bee.energy <= 0:
                self.bees.remove(bee)
                print(f"Bee removed due to low energy. {bee.get_info()}")
            else:
                if random.random() < 0.5:
                    print(bee.work())
                else:
                    print(bee.eat())
        if random.random() < 0.2:
            self.produce_honey(random.randint(1, 5))
        else:
            self.consume_honey(random.randint(1, 5))


# Create a colony with 1000 honey
colony = Colony(1000)

# Add bees to the colony
for _ in range(20):
    bee = Bee('drone', 'mate', 10, 2)
    colony.add_bee(bee)
for _ in range(15):
    bee = Bee('worker', 'gatherer', 10, 2)
    colony.add_bee(bee)
for _ in range(15):
    bee = Bee('worker', 'caretaker', 10, 2)
    colony.add_bee(bee)
for _ in range(1):
    bee = Bee('queen', 'lay egg', 15, 5)
    colony.add_bee(bee)

# Simulate a day in the colony
colony.simulate_day()