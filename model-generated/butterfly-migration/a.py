import random

class Butterfly:
    def __init__(self, species, age, location):
        self.species = species
        self.age = age
        self.location = location
        self.migration_distance = random.randint(10, 50)

    def migrate(self):
        self.location += self.migration_distance

    def age_up(self):
        self.age += 1

    def die(self):
        if self.age > 5:  # Simulating a lifespan of 5 years
            return True
        else:
            return False

class ButterflyPopulation:
    def __init__(self, population_size, species, location):
        self.population = [Butterfly(species, 0, location) for _ in range(population_size)]

    def simulate_migration(self):
        for butterfly in self.population:
            butterfly.migrate()

    def simulate_aging(self):
        for butterfly in self.population:
            butterfly.age_up()

    def simulate_death(self):
        self.population = [butterfly for butterfly in self.population if not butterfly.die()]

    def get_average_lifespan(self):
        total_age = sum(butterfly.age for butterfly in self.population)
        return total_age / len(self.population)

    def get_average_migration_distance(self):
        total_migration_distance = sum(butterfly.migration_distance for butterfly in self.population)
        return total_migration_distance / len(self.population)

    def get_population_size(self):
        return len(self.population)


# Demonstration
population = ButterflyPopulation(100, 'Monarch', 0)

for _ in range(10):  # Simulating 10 years
    population.simulate_migration()
    population.simulate_aging()
    population.simulate_death()

print(f"Average lifespan: {population.get_average_lifespan()} years")
print(f"Average migration distance: {population.get_average_migration_distance()} units")
print(f"Population size: {population.get_population_size()}")