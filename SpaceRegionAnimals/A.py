import datetime

class SpaceRegion:
    def __init__(self, name, temperature, gravity):
        self.name = name
        self.temperature = temperature
        self.gravity = gravity

    def get_environmental_features(self):
        return f"Temperature: {self.temperature}°C, Gravity: {self.gravity}g"

class Animal:
    def __init__(self, species, space_region, date_of_discovery, id):
        self.species = species
        self.space_region = space_region
        self.date_of_discovery = date_of_discovery
        self.id = id

    def get_info(self):
        return f"Species: {self.species}, Space Region: {self.space_region.name}, Date of Discovery: {self.date_of_discovery}, ID: {self.id}"

def find_animals_by_space_region(space_region):
    animals = []
    for animal in animals_list:
        if animal.space_region == space_region:
            animals.append(animal)
    return animals

def find_animals_by_timeframe(start_date, end_date):
    animals = []
    for animal in animals_list:
        if start_date <= animal.date_of_discovery <= end_date:
            animals.append(animal)
    return animals

# Example usage:
space_regions = [
    SpaceRegion("Alpha Centauri", 20, 0.8),
    SpaceRegion("Andromeda", 10, 1.2),
    SpaceRegion("Milky Way", 25, 1.0)
]

animals_list = [
    Animal("Gloopernaught", space_regions[0], datetime.date(2020, 1, 1), 1),
    Animal("Sparklebug", space_regions[1], datetime.date(2021, 6, 15), 2),
    Animal("Fuzzlewhump", space_regions[2], datetime.date(2019, 3, 22), 3),
    Animal("Glimmerwing", space_regions[0], datetime.date(2020, 8, 10), 4),
    Animal("Frozenstalker", space_regions[1], datetime.date(2022, 2, 28), 5)
]

# Find all animals spotted in Alpha Centauri
alpha_centauri_animals = find_animals_by_space_region(space_regions[0])
print(alpha_centauri_animals)

# Find all animals discovered between 2020-01-01 and 2021-12-31
timeframe_animals = find_animals_by_timeframe(datetime.date(2020, 1, 1), datetime.date(2021, 12, 31))
print(timeframe_animals)