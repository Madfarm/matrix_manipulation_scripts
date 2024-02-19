class Island:
    def __init__(self, question, energy_cost, energy_gain):
        self.question = question
        self.energy_cost = energy_cost
        self.energy_gain = energy_gain

class Philosopher:
    def __init__(self, initial_energy, thoughts=[]):
        self.thoughts = thoughts
        self.knowledge = {}
        self.energy = initial_energy
        self.islands = []  # list of Islands to visit

    def visit_island(self, island):
        if self.energy < island.energy_cost:
            return False
        self.thoughts.append(island.question)
        if island.question in self.knowledge:
            self.energy += island.energy_gain
        else:
            self.energy -= island.energy_cost
        return True

    def can_reach_islands(self):
        for island in self.islands:
            if not self.visit_island(island):
                return False
        return True


island1 = Island("What is the meaning of life?", 5, 10)
island2 = Island("Is free will an illusion?", 3, 5)
island3 = Island("Can machines think?", 8, 12)

philosopher = Philosopher(15)
philosopher.islands = [island1, island2, island3]

print(philosopher.can_reach_islands())  # True

philosopher.energy = 10
print(philosopher.can_reach_islands())  # False (not enough energy to visit island2)

philosopher.energy = 20
print(philosopher.can_reach_islands())  # True