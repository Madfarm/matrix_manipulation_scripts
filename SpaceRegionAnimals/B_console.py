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

def add_animal():
    species = input("Enter species name: ")
    space_region_name = input("Enter space region name: ")
    date_of_discovery = datetime.date.today()  # default to today's date
    id = len(animals_list) + 1  # assign a new ID

    # find the space region object
    space_region = next((region for region in space_regions if region.name == space_region_name), None)
    if space_region is None:
        print(f"Error: Space region '{space_region_name}' not found!")
        return

    # create a new animal object
    animal = Animal(species, space_region, date_of_discovery, id)
    animals_list.append(animal)
    print(f"Added animal: {animal.get_info()}")

def find_animals_by_region():
    region_name = input("Enter space region name: ")
    region = next((region for region in space_regions if region.name == region_name), None)
    if region is None:
        print(f"Error: Space region '{region_name}' not found!")
        return

    animals = find_animals_by_space_region(region)
    if len(animals) == 0:
        print(f"No animals found in region '{region.name}'")
    else:
        print("Animals found in region '{region.name}':")
        for animal in animals:
            print(animal.get_info())

def find_animals_by_timeframe():
    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    start_date = datetime.date.fromisoformat(start_date_str)

    end_date_str = input("Enter end date (YYYY-MM-DD): ")
    end_date = datetime.date.fromisoformat(end_date_str)

    animals = find_animals_by_timeframe(start_date, end_date)
    if len(animals) == 0:
        print(f"No animals found in timeframe '{start_date_str}' to '{end_date_str}'")
    else:
        print("Animals found in timeframe '{start_date_str}' to '{end_date_str}':")
        for animal in animals:
            print(animal.get_info())

# init space regions
space_regions = [
    SpaceRegion("Alpha Centauri", 20, 0.8),
    SpaceRegion("Andromeda", 10, 1.2),
    SpaceRegion("Milky Way", 25, 1.0)
]

# init animals list
animals_list = []

while True:
    print("Menu:")
    print("  A) Add animal")
    print("  R) Find animals by region")
    print("  T) Find animals by timeframe")
    print("  Q) Quit")

    choice = input("Enter choice: ")

    if choice.lower() == "a":
        add_animal()
    elif choice.lower() == "r":
        find_animals_by_region()
    elif choice.lower() == "t":
        find_animals_by_timeframe()
    elif choice.lower() == "q":
        break
    else:
        print("Invalid choice!")
