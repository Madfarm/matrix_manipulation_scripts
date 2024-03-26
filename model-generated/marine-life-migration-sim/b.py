class MarineAnimal:
    def __init__(self, id, species, start_point, end_point, duration):
        self.id = id
        self.species = species
        self.start_point = start_point
        self.end_point = end_point
        self.duration = duration

    def migrate(self):
        print(f"{self.species} is migrating from {self.start_point} to {self.end_point} for {self.duration} days.")

class AquaticSimulation:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def simulate(self):
        for animal in self.animals:
            animal.migrate()

# Create a list to store marine animals
marine_animals = []

# Create a few marine animals
marine_animals.append(MarineAnimal(1, "Dolphin", "Atlantic Ocean", "Indian Ocean", 30))
marine_animals.append(MarineAnimal(2, "Whale", "Pacific Ocean", "Arctic Ocean", 60))
marine_animals.append(MarineAnimal(3, "Seal", "Arctic Ocean", "Antarctic Ocean", 90))

# Create an aquatic simulation
simulation = AquaticSimulation()

# Add the marine animals to the simulation
for animal in marine_animals:
    simulation.add_animal(animal)

# Simulate the migration
simulation.simulate()