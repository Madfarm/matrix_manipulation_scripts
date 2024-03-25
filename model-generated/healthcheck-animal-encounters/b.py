import pandas as pd
import numpy as np
import random

# Define the animal species
class Animal:
    def __init__(self, name, species, age, health):
        self.name = name
        self.species = species
        self.age = age
        self.health = health

# Define the encounter class
class Encounter:
    def __init__(self, date, location, species1, species2, interaction):
        self.date = date
        self.location = location
        self.species1 = species1
        self.species2 = species2
        self.interaction = interaction

# Create a list of animals
animals = [Animal('Lion', 'Lion', 5, 100), Animal('Elephant', 'Elephant', 10, 100), Animal('Giraffe', 'Giraffe', 7, 100)]

# Create a list of locations
locations = ['Savannah', 'Forest', 'Desert']

# Create a list of interactions
interactions = ['Friendly', 'Aggressive', 'Neutral']

# Create a DataFrame to store encounters
encounters_df = pd.DataFrame(columns=['Date', 'Location', 'Species1', 'Species2', 'Interaction'])

# Function to simulate an encounter
def simulate_encounter():
    # Select two random animals
    animal1 = random.choice(animals)
    animal2 = random.choice(animals)

    # Select a random location
    location = random.choice(locations)

    # Select a random interaction
    interaction = random.choice(interactions)

    # Create an encounter
    encounter = Encounter(pd.Timestamp.now(), location, animal1.species, animal2.species, interaction)

    # Add the encounter to the DataFrame
    encounters_df.loc[len(encounters_df)] = [encounter.date, encounter.location, encounter.species1, encounter.species2, encounter.interaction]

    # Impact the health of the animals based on the interaction
    if interaction == 'Aggressive':
        animal1.health -= 10
        animal2.health -= 10
    elif interaction == 'Friendly':
        animal1.health += 5
        animal2.health += 5

# Simulate 10 encounters
for _ in range(10):
    simulate_encounter()

# Print the encounters DataFrame
print(encounters_df)

# Print the health of each animal
for animal in animals:
    print(f'{animal.name} ({animal.species}): {animal.health}')