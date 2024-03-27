import pandas as pd

# Define the footprints for each animal species
footprints = {
    'Lion': [[1, 1, 1, 1, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 0, 0, 0, 1],
             [1, 1, 1, 1, 1]],
    'Elephant': [[1, 1, 1, 1, 1],
                 [1, 1, 0, 1, 1],
                 [1, 0, 0, 0, 1],
                 [1, 1, 0, 1, 1],
                 [1, 1, 1, 1, 1]],
    # Define footprints for 8 more species...
}

# Function to identify the animal species based on the footprint
def identify_species(footprint):
    for species, pattern in footprints.items():
        if np.array_equal(pattern, footprint):
            return species
    return 'Unknown species'

# Test the function with a lion footprint
lion_footprint = [[1, 1, 1, 1, 1],
                  [1, 0, 0, 0, 1],
                  [1, 0, 0, 0, 1],
                  [1, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1]]
print(identify_species(lion_footprint))  # Output: Lion