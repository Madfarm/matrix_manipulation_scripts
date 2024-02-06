class Animal:
    def __init__(self, name, species, habitat):
        self.name = name
        self.species = species
        self.habitat = habitat

    def describe(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Habitat: {self.habitat}")

class Bird(Animal):
    def __init__(self, name, species, habitat, magical_ability):
        super().__init__(name, species, habitat)
        self.magical_ability = magical_ability

    def describe(self):
        super().describe()
        print(f"Magical Ability: {self.magical_ability}")

class Mammal(Animal):
    def __init__(self, name, species, habitat, magical_ability):
        super().__init__(name, species, habitat)
        self.magical_ability = magical_ability

    def describe(self):
        super().describe()
        print(f"Magical Ability: {self.magical_ability}")

class EnchantedForest:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, name):
        self.animals = [a for a in self.animals if a.name != name]

    def display_animals(self):
        for animal in self.animals:
            animal.describe()
            print("-" * 10)

    def find_by_name(self, name):
        return [a for a in self.animals if a.name == name]

    def find_by_species(self, species):
        return [a for a in self.animals if a.species == species]

    def find_by_ability(self, ability):
        return [a for a in self.animals if a.magical_ability == ability]


forest = EnchantedForest()

sparkles = Bird("Sparkles", "Phoenix", "Volcanic Mountains", "Rebirth")
whiskers = Mammal("Whiskers", "Shapeshifter Cat", "Mossy Caves", "Shapeshifting")

forest.add_animal(sparkles)
forest.add_animal(whiskers)

forest.display_animals()

print(forest.find_by_ability("Shapeshifting")) 