class Animal:
    def __init__(self, species, diet, habitat, lifespan, age, identifier):
        self.species = species
        self.diet = diet
        self.habitat = habitat
        self.lifespan = lifespan
        self.age = age
        self.identifier = identifier

class AnimalDatabase:
    def __init__(self):
        self.database = []

    def add_animal(self, animal):
        self.database.append(animal)

    def delete_animal(self, identifier):
        for animal in self.database:
            if animal.identifier == identifier:
                self.database.remove(animal)
                break

    def search_by_attribute(self, attribute, value):
        result = [animal for animal in self.database if getattr(animal, attribute) == value]
        return result

# Example usage:

db = AnimalDatabase()

# Adding animals
db.add_animal(Animal("Lion", "Carnivore", "Savannah", 20, 10, "A001"))
db.add_animal(Animal("Elephant", "Herbivore", "Savannah", 60, 30, "A002"))
db.add_animal(Animal("Giraffe", "Herbivore", "Savannah", 30, 15, "A003"))

# Deleting an animal
db.delete_animal("A001")

# Searching by attribute
print(db.search_by_attribute("species", "Lion"))  # Returns a list of lions
print(db.search_by_attribute("diet", "Herbivore"))  # Returns a list of herbivores