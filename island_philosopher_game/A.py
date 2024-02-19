import random

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

    def can_reach_islands(self, islands):
        return all(self.visit_island(island) for island in islands)
    
class Island:
    def __init__(self, question, energy_cost, energy_gain):
        self.question = question
        self.energy_cost = energy_cost
        self.energy_gain = energy_gain

    def __repr__(self):
        return f"Island('{self.question}', {self.energy_cost}, {self.energy_gain})"
    

island1 = Island("What is the meaning of life?", 5, 10)  # energy cost = 5, energy gain = 10
island2 = Island("Is free will an illusion?", 3, 5)  # energy cost = 3, energy gain = 5
island3 = Island("Can machines think?", 8, 12)  # energy cost = 8, energy gain = 12

philosopher = Philosopher(15)  # initial energy = 15

print(philosopher.visit_island(island1))  # True
print(philosopher.thoughts)  # ["What is the meaning of life?"]
print(philosopher.energy)  # 20

print(philosopher.visit_island(island2))  # True
print(philosopher.thoughts)  # ["What is the meaning of life?", "Is free will an illusion?"]
print(philosopher.energy)  # 22

print(philosopher.visit_island(island3))  # False
print(philosopher.thoughts)  # ["What is the meaning of life?", "Is free will an illusion?"]
print(philosopher.energy)  # 22

print(philosopher.can_reach_islands([island1, island2]))  # True
print(philosopher.can_reach_islands([island1, island2, island3]))  # False