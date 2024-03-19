import random

# Define the ingredients
caffeine_range = (70, 300)
amino_acids = ['L-leucine', 'L-isoleucine', 'L-valine', 'L-lysine', 'L-threonine', 'L-phenylalanine', 'L-histidine', 'L-methionine', 'L-tryptophan']
sugar_range = (0, 120)
vitamins = ['Vitamin B6', 'Vitamin B12', 'Niacin', 'Pantothenic acid', 'Vitamin B5', 'Folic acid', 'Biotin', 'Vitamin B2', 'Vitamin B1']
flavors = ['Tropical', 'Berry', 'Citrus', 'Fruit Punch', 'Grape', 'Orange', 'Cola', 'Mint', 'Lemon', 'Pineapple']

# Function to generate an energy drink
def generate_energy_drink():
    energy_drink = {
        'caffeine': random.randint(*caffeine_range),
        'amino_acids': random.sample(amino_acids, 3),
        'sugar': random.randint(*sugar_range),
        'vitamins': random.sample(vitamins, 3),
        'flavor': random.choice(flavors)
    }
    return energy_drink

# Generate 5 energy drinks
for _ in range(5):
    print(generate_energy_drink())