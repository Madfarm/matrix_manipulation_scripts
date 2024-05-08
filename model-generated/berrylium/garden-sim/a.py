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
    def __init__(self, name, plant_type, color, bloom_season, nectar_production):        
        self.name = name
        self.plant_type = plant_type
        self.color = color
        self.bloom_season = bloom_season
        self.nectar_production = nectar_production
        self.is_blooming = False
        self.current_bloom_time = None

    def __str__(self):
        return f"{self.name} ({self.plant_type.name}, {self.color}, {self.bloom_season})"
        
    def bloom(self):
        if self.bloom_season.value[0] <= Season.current_season <= self.bloom_season.value[1]:
            self.is_blooming = True
            self.current_bloom_time = datetime.now()
        else:
            self.is_blooming = False
            self.current_bloom_time = None

    def time_till_bloom(self):
        if not self.is_blooming and self.current_bloom_time:
            return (self.current_bloom_time - datetime.now()).days
        return 0

class Bee:
    def __init__(self, name, species, preference):        
        self.name = name
        self.species = species
        self.preference = preference
        self.current_flower = None
        self.energy = 100

    def __str__(self):
        return f"{self.name} ({self.species}, {self.preference})"

    def forage(self, garden):
        if self.energy > 0:
            available_flowers = [plant for plant in garden.plants.values() if plant.is_blooming and self.is_attracted_to(plant)]
            if available_flowers:
                self.current_flower = random.choice(available_flowers)
                self.energy -= 5
                print(f"{self.name} is visiting {self.current_flower.name}")
                self.current_flower.nectar_production -= 1
            else:
                print(f"{self.name} couldn't find any suitable flower to visit.")
                self.energy -= 2
        else:
            print(f"{self.name} is tired and needs to rest.")

    def is_attracted_to(self, plant):
        if self.preference == PlantType.ALL:
            return True
        return plant.plant_type == self.preference

    def rest(self):
        if self.energy < 100:
            self.energy += 20
            print(f"{self.name} is resting and regaining energy.")      

class Butterfly:
    def __init__(self, name, species, preference, flutter_duration):        
        self.name = name
        self.species = species
        self.preference = preference
        self.flutter_duration = flutter_duration
        self.current_flower = None  

    def __str__(self):
        return f"{self.name} ({self.species}, {self.preference})"
    def flutter(self, garden):
        if self.energy > 0:
            available_flowers = [plant for plant in garden.plants.values()
                                 if plant.is_blooming and self.is_attracted_to(plant)]
            if available_flowers:
                self.current_flower = random.choice(available_flowers)  
                print(f"{self.name} is fluttering to {self.current_flower.name}")              
                self.energy -= 1
                self.current_flower.nectar_production -= 1
                time.sleep(self.flutter_duration)
            else:
                print(f"{self.name} couldn't find any suitable flower to flutter to.")      
                self.energy -= 1
        else:
            print(f"{self.name} is tired and needs to rest.")   
    
    def is_attracted_to(self, plant):
        return plant.color in self.preference

    @property
    def energy(self):
        return 100 - (datetime.now() - self.last_flutter_time).seconds // 10

    @energy.setter
    def energy(self, value):
        self.last_flutter_time = datetime.now()

class Garden: 
    def __init__(self, size):      
        self.size = size
        self.plants = {}        
        self.pollinators = {}   
        self.season = Season.SPRING

    def add_plant(self, plant):
        if len(self.plants) < self.size:            
            self.plants[plant.name] = plant        
        else:
            print(f"Garden is full, can't add {plant.name}")
    
    def add_pollinator(self, pollinator):
        self.pollinators[pollinator.name] = pollinator

    def simulate_a_day(self):
        print(f"\n--- A New Day in the Garden ---")
        print(f"Current Season: {self.season}")
        # Update plant status
        for plant in self.plants.values():            
            plant.bloom()
        
        # Update pollinator activities
        for _, pollinator in self.pollinators.items():           
            if isinstance(pollinator, Bee):
                pollinator.forage(self)     
                pollinator.rest()   
            else:   
                pollinator.flutter(self)
        # Change season if necessary
        self.update_season()

    def update_season(self):
        if Season.current_season == Season.WINTER:
            Season.current_season = Season.SPRING
        else:
            Season.current_season += 1 

    def plot_garden(self):
        print("*" * 30)
        print(" Garden Plot ")
        print("*" * 30)
        for plant_name in self.plants:
            print(f"{self.plants[plant_name]}")

    def apply_pesticide(self):
        print("Applying pesticide to the garden...")
        for _, plant in self.plants.items():
            plant.nectar_production //= 2  # Reduce nectar production by half

    def choose_plants(self):
        print("Available Plant Options:")
        for plant_type in PlantType:
            print(f"{plant_type.value}: {plant_type.name}")
        user_input = PlantType(input("Choose a plant to add (or 'Q' to quit): "))
        if user_input != PlantType.ALL:
            plant_name = input("Enter a name for the plant: ")
            self.add_plant(Plant(plant_name, user_input, random.choice(["Red", "Yellow", "Blue"]),random.choice([(Season.SPRING, Season.SUMMER), (Season.SUMMER, Season.AUTUMN), (Season.AUTUMN, Season.WINTER)]), random.randint(10,20)))
        
    def tend_to_garden(self):
        while True:
            self.simulate_a_day()
            self.plot_garden()  
            print("Pollinator Activities:")
            for _, pollinator in self.pollinators.items():               
                print(f"{pollinator}")
            print("*"*50)  
            choice = input("""
            Menu:
            'A' - Add a new plant
            'P' - Apply pesticide
            'T' - Tend to the garden (simulate a day)
            'Q' - Quit 
            Enter your choice: """)
            if choice == 'A':
                self.choose_plants()
            elif choice == 'P':
                self.apply_pesticide()
            elif choice == 'T':
                pass  # Already handled
            elif choice == 'Q':
                print("Goodbye! Visiting the garden again soon.")
                break
            else:
                print("Invalid choice. Please try again.")   


class Season(Enum):
    SPRING = (1, 3) 
    SUMMER = (4, 6)  
    AUTUMN = (7, 9)  
    WINTER = (10, 12)  
    @property    
    def current_season(self):
        return getattr(self, '_current_season', self.SPRING) 
    @current_season.setter
    def current_season(self, value):        
        if value in Season: 
            self._current_season = value     
        else:
            raise ValueError(f"Invalid season: {value}") 

# Initialize the garden
garden_size = 10
garden = Garden(garden_size)       

# Add some default plants
garden.add_plant(Plant("Rose", PlantType.ROSE, "Red", (Season.SPRING, Season.AUTUMN), 15))
garden.add_plant(Plant("Sunflower", PlantType.SUNFLOWER, "Yellow", (Season.SUMMER, Season.AUTUMN), 20))

# Add some pollinators
garden.add_pollinator(Bee("Buzz", "Bumblebee", PlantType.ALL))
garden.add_pollinator(Butterfly("Flutterby", "Monarch", ["Yellow", "Orange"], 0.5))

# Start the gardening simulation
garden.tend_to_garden()