import random

# Define the lists of ingredients
caffeine_range = range(70, 301)
amino_acids = ["L-leucine", "L-isoleucine", "L-valine", "L-lysine", "L-threonine", "L-phenylalanine", "L-histidine", "L-methionine", "L-tryptophan"]
sugar_range = range(0, 121)
vitamins = ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D", "Vitamin E"]
other_ingredients = ["guarana", "taurine", "L-theanine", "creatine"]
flavors = ["Berry Burst", "Citrus Blast", "Fruit Punch", "Grape", "Orange", "Peach", "Pineapple", "Raspberry", "Strawberry", "Tropical"]

# Function to generate a random energy drink
def generate_energy_drink():
    energy_drink = {
        "Caffeine": random.choice(caffeine_range),
        "Amino Acids": random.sample(amino_acids, 3),
        "Sugar": random.choice(sugar_range),
        "Vitamins": random.sample(vitamins, 3),
        "Other Ingredients": random.sample(other_ingredients, 2),
        "Flavor": random.choice(flavors)
    }
    return energy_drink

# Generate and print 5 random energy drinks
for _ in range(5):
    print(generate_energy_drink())