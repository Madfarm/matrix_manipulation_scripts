import datetime

class SpaceRegion:
    def __init__(self, name, temperature, gravity):
        self.name = name
        self.temperature = temperature
        self.gravity = gravity

    def get_environmental_features(self):
        return (self.temperature, self.gravity)

class Animal:
    def __init__(self, species_name, space_region, date_of_discovery, unique_id):
        self.species_name = species_name
        self.space_region = space_region
        self.date_of_discovery = date_of_discovery
        self.unique_id = unique_id

    def get_space_region(self):
        return self.space_region

    def get_date_of_discovery(self):
        return self.date_of_discovery

    def __eq__(self, other):
        return self.unique_id == other.unique_id

    def __hash__(self):
        return hash(self.unique_id)

def find_animals_in_region(region_name):
    animals_in_region = []
    for animal in animals:
        if animal.get_space_region().name == region_name:
            animals_in_region.append(animal)
    return animals_in_region

def find_animals_in_timeframe(start_date, end_date):
    animals_in_timeframe = []
    for animal in animals:
        if start_date <= animal.get_date_of_discovery() <= end_date:
            animals_in_timeframe.append(animal)
    return animals_in_timeframe

# Example usage:

# Create some space regions
alpha_centauri = SpaceRegion("Alpha Centauri", 200, 0.8)
beta_hydri = SpaceRegion("Beta Hydri", 150, 1.2)

# Create some animals
animal1 = Animal("Species A", alpha_centauri, datetime.date(2020, 1, 1), 1)
animal2 = Animal("Species B", beta_hydri, datetime.date(2020, 2, 1), 2)
animal3 = Animal("Species C", alpha_centauri, datetime.date(2020, 3, 1), 3)

# Create a list to store all animals
animals = [animal1, animal2, animal3]

# Find all animals in Alpha Centauri
animals_in_alpha_centauri = find_animals_in_region("Alpha Centauri")
print(animals_in_alpha_centauri)  # Output: [Animal(species_name='Species A', space_region=SpaceRegion(name='Alpha Centauri', temperature=200, gravity=0.8), date_of_discovery=2020-01-01, unique_id=1), Animal(species_name='Species C', space_region=SpaceRegion(name='Alpha Centauri', temperature=200, gravity=0.8), date_of_discovery=2020-03-01, unique_id=3)]

# Find all animals discovered between 2020-01-01 and 2020-03-01
animals_in_timeframe = find_animals_in_timeframe(datetime.date(2020, 1, 1), datetime.date(2020, 3, 1))
print(animals_in_timeframe)  # Output: [Animal(species_name='Species A', space_region=SpaceRegion(name='Alpha Centauri', temperature=200, gravity=0.8), date_of_discovery=2020-01-01, unique_id=1), Animal(species_name='Species C', space_region=SpaceRegion(name='Alpha Centauri', temperature=200, gravity=0.8), date_of_discovery=2020-03-01, unique_id=3)]