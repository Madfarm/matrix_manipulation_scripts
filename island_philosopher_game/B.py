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
        self.islands = []  # list of islands to visit

    def visit_island(self, island):
        if self.energy < island.energy_cost:
            return False
        self.thoughts.append(island.question)
        if island.question in self.knowledge:
            self.energy += island.energy_gain
        else:
            self.energy -= island.energy_cost
        return True

    def can_reach_islands(self, islands):
        for island in islands:
            if not self.visit_island(island):
                return False
        return True

    def set_islands(self, islands):
        self.islands = islands

# Create islands
island1 = Island("What is the meaning of life?", 5, 10)
island2 = Island("Is free will an illusion?", 3, 5)
island3 = Island("Can machines think?", 8, 12)

# Create philosopher
philosopher = Philosopher(15)

# Set islands to visit
philosopher.set_islands([island1, island2, island3])

# Test can_reach_islands()
print(philosopher.can_reach_islands())  # Should print True

# Try to visit island3 (which requires 8 energy)
philosopher.visit_island(island3)  # Should print False

# Try to visit island1 (which requires 5 energy)
philosopher.visit_island(island1)  # Should print True

# Try to visit island2 (which requires 3 energy)
philosopher.visit_island(island2)  # Should print True

# Test can_reach_islands() again
print(philosopher.can_reach_islands())  # Should print False (because philosopher doesn't have enough energy to visit island3)