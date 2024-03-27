class Animal:
    def __init__(self, name, type, diet, habitat, num_legs, lifespan):
        self.name = name
        self.type = type
        self.diet = diet
        self.habitat = habitat
        self.num_legs = num_legs
        self.lifespan = lifespan

database = [
    Animal("Lion", "Mammal", "Carnivore", "Savanna", 4, 12),
    Animal("Giraffe", "Mammal", "Herbivore", "Savanna", 4, 20),
    Animal("Snake", "Reptile", "Carnivore", "Forest", 0, 20),
    Animal("Tortoise", "Reptile", "Herbivore", "Desert", 4, 150),
    Animal("Eagle", "Bird", "Carnivore", "Mountain", 2, 20),
    Animal("Penguin", "Bird", "Carnivore", "Antarctica", 2, 20),
    Animal("Salmon", "Fish", "Herbivore", "Ocean", 0, 3),
    Animal("Shark", "Fish", "Carnivore", "Ocean", 0, 20),
    Animal("Butterfly", "Insect", "Herbivore", "Forest", 6, 2),
    Animal("Bee", "Insect", "Carnivore", "Flower", 6, 3)
]

def find_animals(type=None, diet=None, habitat=None, num_legs=None, lifespan=None):
    matching_animals = []
    for animal in database:
        if (type is None or animal.type == type) and \
           (diet is None or animal.diet == diet) and \
           (habitat is None or animal.habitat == habitat) and \
           (num_legs is None or animal.num_legs == num_legs) and \
           (lifespan is None or animal.lifespan == lifespan):
            matching_animals.append(animal.name)
    return matching_animals

# Example usage:
print(find_animals(type="Mammal", diet="Herbivore"))  # Output: ['Giraffe']