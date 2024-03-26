import time

class MarineAnimal:
    def __init__(self, id, species, start_point, end_point, duration):
        self.id = id
        self.species = species
        self.start_point = start_point
        self.end_point = end_point
        self.duration = duration
        self.current_location = start_point
        self.migration_started = False

    def start_migration(self):
        self.migration_started = True
        print(f"{self.species} with ID {self.id} has started migrating from {self.start_point} to {self.end_point}.")

    def update_location(self):
        if self.migration_started:
            if self.current_location != self.end_point:
                self.current_location = "Traveling..."
            else:
                self.current_location = self.end_point
                self.migration_started = False

    def get_location(self):
        return self.current_location

class MarineAnimalSystem:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def run_simulation(self):
        for animal in self.animals:
            if not animal.migration_started:
                animal.start_migration()
            animal.update_location()
            print(f"The current location of {animal.species} with ID {animal.id} is {animal.get_location()}.")
        time.sleep(1)

# Create animals
whale = MarineAnimal(1, "Whale", "Atlantic Ocean", "Pacific Ocean", 30)
shark = MarineAnimal(2, "Shark", "Indian Ocean", "South Pacific Ocean", 20)

# Create system and add animals
system = MarineAnimalSystem()
system.add_animal(whale)
system.add_animal(shark)

# Run simulation - update with loop
system.run_simulation()