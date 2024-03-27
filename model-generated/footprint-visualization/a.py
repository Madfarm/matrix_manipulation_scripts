import pandas as pd

# Define the footprints of each animal species
footprints = {
    'Lion': pd.DataFrame([
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1]
    ]),
    'Tiger': pd.DataFrame([
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ]),
    'Elephant': pd.DataFrame([
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]),
    # Add more species as needed
}

# Function to identify the animal species based on the footprint
def identify_species(footprint):
    for species, species_footprint in footprints.items():
        if species_footprint.equals(footprint):
            return species
    return 'Unknown'

# Test the program with a known footprint
test_footprint = pd.DataFrame([
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1]
])

print(identify_species(test_footprint))  # Output: Lion