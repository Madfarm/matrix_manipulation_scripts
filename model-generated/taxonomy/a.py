class Animal:
    def __init__(self, name, type, diet, habitat, legs, lifespan):
        self.name = name
        self.type = type
        self.diet = diet
        self.habitat = habitat
        self.legs = legs
        self.lifespan = lifespan

# Hardcoded database
animals = [
    Animal('Lion', 'Mammal', 'Carnivore', 'Savanna', 4, 12),
    Animal('Giraffe', 'Mammal', 'Herbivore', 'Savanna', 4, 20),
    Animal('Crocodile', 'Reptile', 'Carnivore', 'Savanna', 4, 70),
    Animal('Zebra', 'Mammal', 'Herbivore', 'Savanna', 4, 25),
    Animal('Elephant', 'Mammal', 'Herbivore', 'Savanna', 4, 70),
    Animal('Gazelle', 'Mammal', 'Herbivore', 'Savanna', 4, 10),
    Animal('Hyena', 'Mammal', 'Omnivore', 'Savanna', 4, 10),
    Animal('Jackal', 'Mammal', 'Omnivore', 'Savanna', 4, 7),
    Animal('Buffalo', 'Mammal', 'Herbivore', 'Savanna', 4, 15),
    Animal('Meerkat', 'Mammal', 'Omnivore', 'Savanna', 4, 15),
    Animal('Warthog', 'Mammal', 'Herbivore', 'Savanna', 4, 20),
    Animal('Cheetah', 'Mammal', 'Carnivore', 'Savanna', 4, 12),
    Animal('Antelope', 'Mammal', 'Herbivore', 'Savanna', 4, 10),
    Animal('Snake', 'Reptile', 'Carnivore', 'Savanna', 0, 10),
    Animal('Lizard', 'Reptile', 'Herbivore', 'Savanna', 4, 20),
]

def find_animals(type=None, diet=None, habitat=None, legs=None, lifespan=None):
    results = []
    for animal in animals:
        if (type is None or animal.type == type) and \
           (diet is None or animal.diet == diet) and \
           (habitat is None or animal.habitat == habitat) and \
           (legs is None or animal.legs == legs) and \
           (lifespan is None or animal.lifespan == lifespan):
            results.append(animal.name)
    return results

# Testing the function
print(find_animals(type='Mammal', diet='Herbivore', habitat='Savanna'))
print(find_animals(type='Reptile', diet='Carnivore', habitat='Savanna'))
print(find_animals(type='Mammal', diet='Omnivore', habitat='Savanna'))