import random

class Butterfly:
    def __init__(self, species, age, location):
        self.species = species
        self.age = age
        self.location = location
        self.lifespan = random.randint(5, 10)  # Random lifespan between 5 and 10 days
        self.migration_distance = random.randint(10, 100)  # Random migration distance between 10 and 100 km

    def migrate(self):
        # Simulate migration by reducing the butterfly's lifespan
        self.lifespan -= 1
        if self.lifespan <= 0:
            return False  # Butterfly dies during migration
        else:
            return True  # Butterfly survives migration

    def live(self):
        # Simulate aging by reducing the butterfly's lifespan
        self.lifespan -= 1
        if self.lifespan <= 0:
            return False  # Butterfly dies of old age
        else:
            return True  # Butterfly continues to live

class Environment:
    def __init__(self, climate, geography, human_interference):
        self.climate = climate
        self.geography = geography
        self.human_interference = human_interference

    def affect_butterfly(self, butterfly):
        # Simulate the environment affecting the butterfly
        if self.climate == 'hot':
            butterfly.lifespan -= 2
        elif self.climate == 'cold':
            butterfly.lifespan -= 1

        if self.geography == 'mountainous':
            butterfly.migration_distance += 20
        elif self.geography == 'swampy':
            butterfly.migration_distance -= 10

        if self.human_interference == 'high':
            butterfly.lifespan -= 3

# Create a population of 100 butterflies
population = [Butterfly('Species A', 0, 'Forest') for _ in range(50)]
population += [Butterfly('Species B', 0, 'Plains') for _ in range(50)]

# Create an environment
environment = Environment('temperate', 'grassland', 'low')

# Simulate the butterflies living and migrating
survived_migrations = 0
survived_aging = 0
for butterfly in population:
    environment.affect_butterfly(butterfly)
    if butterfly.migrate():
        survived_migrations += 1
    if butterfly.live():
        survived_aging += 1

# Print statistics
print(f'Average lifespan: {sum(butterfly.lifespan for butterfly in population) / len(population)} days')
print(f'Average migration distance: {sum(butterfly.migration_distance for butterfly in population) / len(population)} km')
print(f'Butterflies that survived migration: {survived_migrations}')
print(f'Butterflies that survived aging: {survived_aging}')