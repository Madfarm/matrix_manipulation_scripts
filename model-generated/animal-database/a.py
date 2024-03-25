class Animal:
    def __init__(self, species, diet, habitat, lifespan, age, id):
        self.species = species
        self.diet = diet
        self.habitat = habitat
        self.lifespan = lifespan
        self.age = age
        self.id = id

class AnimalDatabase:
    def __init__(self):
        self.animals = []

    def add_animal(self, species, diet, habitat, lifespan, age, id):
        new_animal = Animal(species, diet, habitat, lifespan, age, id)
        self.animals.append(new_animal)

    def delete_animal(self, id):
        self.animals = [animal for animal in self.animals if animal.id != id]

    def search(self, attribute, value):
        return [animal for animal in self.animals if getattr(animal, attribute) == value]

# Create a new database
db = AnimalDatabase()

# Add some animals
db.add_animal('Lion', 'Meat', 'Savannah', 15, 5, 1)
db.add_animal('Elephant', 'Herbs', 'Savannah', 50, 10, 2)
db.add_animal('Giraffe', 'Herbs', 'Savannah', 20, 7, 3)

# Delete an animal
db.delete_animal(2)

# Search for animals
print(db.search('species', 'Lion'))
print(db.search('diet', 'Herbs'))
print(db.search('habitat', 'Savannah'))
print(db.search('lifespan', 15))
print(db.search('age', 7))
print(db.search('id', 1))