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

animals = []
space_regions = []

def add_animal():
    species = input("Enter species name: ")
    space_region_name = input("Enter space region name: ")
    date_of_discovery = datetime.date.today()
    id = len(animals) + 1

    space_region = next((region for region in space_regions if region.name == space_region_name), None)
    if space_region is None:
        print(f"Error: Space region '{space_region_name}' not found.")
        return

    animal = Animal(species, space_region, date_of_discovery, id)
    animals.append(animal)
    print(f"Added animal: {animal.get_info()}")

def add_space_region():
    name = input("Enter space region name: ")
    temperature = int(input("Enter temperature (°C): "))
    gravity = int(input("Enter gravity (g): "))

    space_region = SpaceRegion(name, temperature, gravity)
    space_regions.append(space_region)
    print(f"Added space region: {space_region.name}")

def find_animals_by_region():
    space_region_name = input("Enter space region name: ")
    space_region = next((region for region in space_regions if region.name == space_region_name), None)
    if space_region is None:
        print(f"Error: Space region '{space_region_name}' not found.")
        return

    animals_in_region = [animal for animal in animals if animal.space_region == space_region]
    if len(animals_in_region) == 0:
        print(f"No animals found in region '{space_region_name}'.")
    else:
        print("Animals found in region '{space_region_name}':")
        for animal in animals_in_region:
            print(animal.get_info())

def find_animals_by_timeframe():
    start_date = datetime.date.today() - datetime.timedelta(days=30)
    end_date = datetime.date.today()

    start_date_str = input(f"Enter start date (YYYY-MM-DD): ")
    end_date_str = input(f"Enter end date (YYYY-MM-DD): ")

    try:
        start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please enter dates in the format YYYY-MM-DD.")
        return

    animals_in_timeframe = [animal for animal in animals if start_date <= animal.date_of_discovery <= end_date]
    if len(animals_in_timeframe) == 0:
        print(f"No animals found in timeframe '{start_date_str}' to '{end_date_str}'.")
    else:
        print(f"Animals found in timeframe '{start_date_str}' to '{end_date_str}':")
        for animal in animals_in_timeframe:
            print(animal.get_info())

def display_all_animals():
    print("All animals:")
    for animal in animals:
        print(animal.get_info())

print("Welcome to the Animal Tracker console application!")

while True:
    print("""
    Menu:
    1. Add animal
    2. Add space region
    3. Find animals by region
    4. Find animals by timeframe
    5. Display all animals
    6. Quit
    """)

    choice = input("Enter choice: ")

    if choice == "1":
        add_animal()
    elif choice == "2":
        add_space_region()
    elif choice == "3":
        find_animals_by_region()
    elif choice == "4":
        find_animals_by_timeframe()
    elif choice == "5":
        display_all_animals()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")