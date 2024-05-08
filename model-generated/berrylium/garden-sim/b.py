import random
import time
from collections import defaultdict
from datetime import datetime, timedelta
from enum import Enum

class PlantType(Enum):
    ROSE = 1
    SUNFLOWER = 2
    TULIP = 3
    DAFFODIL = 4
    VIOLET = 5
    LANTANA = 6

class Plant:
    def __init__(self, plant_type, name, color, bloom_season, nectar_production):
        self.plant_type = plant_type
        self.name = name
        self.color = color
        self.bloom_season = bloom_season
        self.nectar_production = nectar_production
        self.is_blooming = False
        
    def __str__(self):
        return f"{self.name} ({self.plant_type.name}, {self.color}, {self.bloom_season})"
    
    def bloom(self):
        self.is_blooming = True
        
    def wither(self):
        self.is_blooming = False

class Pollinator:
    def __init__(self, name, species, preference):
        self.name = name
        self.species = species
        self.preference = preference
        self.current_plant = None
        self.energy = 100

    def __str__(self):
        return f"{self.name} ({self.species})"
    
    def feed(self, plant):
        if plant.nectar_production > 0:
            self.energy += plant.nectar_production
            plant.nectar_production -= 1
        if self.energy > 150:
            self.energy = 100  # Cap energy at 100

    def find_food(self, garden):
        available_plants = [plant for plant in garden.plants.values() if plant.is_blooming and plant.plant_type in self.preference]
        if available_plants:
            plant = random.choice(available_plants)
            self.current_plant = plant
            return plant
        else:
            return None
    
    def move(self):
        pass  # You can implement pollinator movement later


class Bee(Pollinator):
    def __init__(self, name):
        super().__init__(name, "Bee", {PlantType.ROSE, PlantType.TULIP, PlantType.LANTANA})


class Butterfly(Pollinator):
    def __init__(self, name):
        super().__init__(name, "Butterfly", {PlantType.SUNFLOWER, PlantType.VIOLET})


class Garden:
    def __init__(self, size):
        self.size = size
        self.plants = {}
        self.pollinators = {}
        self.current_season = Season.SPRING
        
    def add_plant(self, plant):
        if len(self.plants) < self.size:
            self.plants[plant.name] = plant
        else:
            print(f"Garden is full, cannot add {plant.name}.")
            
    def add_pollinator(self, pollinator):
        self.pollinators[pollinator.name] = pollinator
        
    def season_update(self):
        # Progress through seasons in a loop
        next_season = (Season(self.current_season.value + 1)) % 4
        self.current_season = next_season
        print(f"\n-- It's now {self.current_season.name} season! --")
        
        # Wither plants and update bloom status
        for plant in self.plants.values():
            if self.current_season in plant.bloom_season:
                plant.bloom()
            else:
                plant.wither()
    
    def pollinator_activity(self):
        for _ in range(10):  # 10 units of activity
            for pollinator in self.pollinators.values():
                pollinator.energy = 100  # Reset energy at the start of activity
                plant = pollinator.find_food(self)
                if plant:
                    pollinator.feed(plant)
                    pollinator.move()
                else:
                    pollinator.current_plant = None
    
    def print_garden_status(self):
        print("\n**Garden Status:**")
        print("Plants:")
        for plant in self.plants.values():
            print(f"  {plant}")
        print("Pollinators:")
        for pollinator in self.pollinators.values():
            print(f"  {pollinator} - Current Plant: {pollinator.current_plant} - Energy: {pollinator.energy}")

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

# Define plant attributes
plant_attributes = {
    PlantType.ROSE:       Plant(PlantType.ROSE, "Rose", "Red",   {Season.SPRING, Season.SUMMER}, 20),
    PlantType.SUNFLOWER:  Plant(PlantType.SUNFLOWER, "Sunflower", "Yellow", {Season.SUMMER, Season.AUTUMN}, 30),
    PlantType.TULIP:     Plant(PlantType.TULIP, "Tulip", "Orange", {Season.SPRING}, 25),
    PlantType.DAFFODIL:  Plant(PlantType.DAFFODIL, "Daffodil", "Yellow", {Season.SPRING}, 15),
    PlantType.VIOLET:    Plant(PlantType.VIOLET, "Violet", "Purple", {Season.SPRING, Season.AUTUMN}, 10),
    PlantType.LANTANA:   Plant(PlantType.LANTANA, "Lantana", "Red-Orange", {Season.SUMMER, Season.AUTUMN}, 28),       
}        
        
def user_plant_selection():
    print("\n-- Choose Plants for Your Garden --")
    plant_choices = {k.value: v for k, v in plant_attributes.items()}
    for choice_id, plant in plant_choices.items():
        print(f"{choice_id}: {plant}")
    
    selected_plants = []
    while True:
        user_input = input("Enter the number(s) of the plants you want to add separated by space, or 'done' to finish: ")
        if user_input.lower() == "done":
            break
        plant_ids = user_input.split()
        for plant_id in plant_ids:
            if plant_id not in plant_choices.keys():
                print(f"Invalid plant choice. Please select from the given options.")
            else:
                selected_plants.append(plant_choices[int(plant_id)])
    return selected_plants

def user_pollinator_selection():
    print("\n-- Choose Pollinators for Your Garden --")
    num_pollinators = int(input("How many pollinators do you want to add (Bee or Butterfly)? "))
    pollinators = []
    for _ in range(num_pollinators):
        pollinator_type = input("Enter 'B' for Bee or 'BUT' for Butterfly: ").upper()
        while pollinator_type not in ("B", "BUT"):
            pollinator_type = input("Invalid input. Please enter 'B' for Bee or 'BUT' for Butterfly: ").upper()
        name = input("Enter the name of the pollinator: ")
        if pollinator_type == "B":
            pollinators.append(Bee(name))
        else:
            pollinators.append(Butterfly(name))
    return pollinators  

def main():
    garden_size = int(input("Welcome to the Pollinator Paradise! How big is your garden (max 10 plants)? "))
    garden = Garden(garden_size)
    
    selected_plants = user_plant_selection()
    for plant in selected_plants:
        garden.add_plant(plant)
    
    selected_pollinators = user_pollinator_selection()
    for pollinator in selected_pollinators:
        garden.add_pollinator(pollinator)
        
    print("\n-- Your Garden is Ready! --")
    
    for _ in range(10):  # Simulate 10 seasons
        garden.season_update()
        garden.pollinator_activity()
        garden.print_garden_status()
        time.sleep(2)  # Delay for visual effect
    input("\nPress Enter to exit...")
        

if __name__ == "__main__":
    main()