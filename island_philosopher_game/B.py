class Island:
    def __init__(self, question, energy_cost, energy_gain):
        self.question = question
        self.energy_cost = energy_cost
        self.energy_gain = energy_gain

islands = [
    Island("What is the meaning of life?", 5, 10),
    Island("Is free will an illusion?", 3, 5),
    Island("Can machines think?", 8, 12)
]

class Philosopher:
    def __init__(self, initial_energy, thoughts=[]):
        self.thoughts = thoughts
        self.knowledge = {}
        self.energy = initial_energy

    def visit_island(self, island):
        if self.energy < island.energy_cost:
            return False
        self.thoughts.append(island.question)
        if island.question in self.knowledge:
            self.energy += island.energy_gain
        else:
            self.energy -= island.energy_cost
        return True

    def can_reach_island(self, island):
        for prev_island in islands[: islands.index(island)]:
            if not self.visit_island(prev_island):
                return False
        return self.visit_island(island)

philosopher = Philosopher(15)

print(philosopher.can_reach_island(islands[0]))  # True
print(philosopher.can_reach_island(islands[1]))  # True
print(philosopher.can_reach_island(islands[2]))  # False (not enough energy to visit island2)

philosopher.energy = 20
print(philosopher.can_reach_island(islands[2]))  # True