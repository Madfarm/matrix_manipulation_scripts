import pandas as pd
import numpy as np
import random

# Initialize animals
animals = pd.DataFrame({
    'name': ['Lion', 'Giraffe', 'Elephant', 'Zebra', 'Hyena'],
    'species': ['Lion', 'Giraffe', 'Elephant', 'Zebra', 'Hyena'],
    'age': [5, 7, 4, 3, 2],
    'health': [100, 90, 80, 70, 60]
})

# Initialize encounters
encounters = pd.DataFrame({
    'date': pd.date_range(start='1/1/2024', periods=5),
    'location': ['Savannah', 'Forest', 'Desert', 'Mountain', 'Wetland'],
    'species1': ['Lion', 'Giraffe', 'Elephant', 'Zebra', 'Hyena'],
    'species2': ['Zebra', 'Hyena', 'Lion', 'Giraffe', 'Elephant'],
    'encounter_type': ['friendly', 'aggressive', 'neutral', 'friendly', 'aggressive']
})

# Function to update animal health after encounter
def update_health(species, encounter_type):
    global animals
    if encounter_type == 'aggressive':
        animals.loc[animals['species'] == species, 'health'] -= 10
    elif encounter_type == 'neutral':
        animals.loc[animals['species'] == species, 'health'] -= 5
    elif encounter_type == 'friendly':
        animals.loc[animals['species'] == species, 'health'] += 5

# Simulate encounters
for index, row in encounters.iterrows():
    update_health(row['species1'], row['encounter_type'])
    update_health(row['species2'], row['encounter_type'])

# Get the location with the most encounters
most_common_location = encounters['location'].mode()[0]

print("Animals after encounters:")
print(animals)
print("Most common location:", most_common_location)