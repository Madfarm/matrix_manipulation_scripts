class Animal:
    def __init__(self, name, species, language):
        self.name = name
        self.species = species
        self.language = language

    def __str__(self):
        return f"Name: {self.name}, Species: {self.species}, Language: {self.language}"

class Language:
    def __init__(self, name, characters, grammar_rules):
        self.name = name
        self.characters = characters
        self.grammar_rules = grammar_rules

    def __str__(self):
        return f"Name: {self.name}, Characters: {self.characters}, Grammar Rules: {self.grammar_rules}"

class Forest:
    def __init__(self):
        self.animals = {}

    def add_animal(self, animal):
        self.animals[animal.name] = animal

    def update_animal(self, name, species, language):
        if name in self.animals:
            self.animals[name] = Animal(name, species, language)
        else:
            print("Animal not found.")

    def search_animal_by_name(self, name):
        if name in self.animals:
            return self.animals[name]
        else:
            return "Animal not found."

    def search_animal_by_language(self, language):
        for animal in self.animals.values():
            if animal.language == language:
                return animal
        return "Animal not found."

# Create animals and languages
lion_language = Language("Lion", "abc", "Subject-Verb-Object")
lion = Animal("Simba", "Lion", lion_language)

giraffe_language = Language("Giraffe", "def", "Subject-Object-Verb")
giraffe = Animal("Balthazar", "Giraffe", giraffe_language)

# Create the forest and add animals
forest = Forest()
forest.add_animal(lion)
forest.add_animal(giraffe)

# Search for animals by name
print(forest.search_animal_by_name("Simba"))
print(forest.search_animal_by_name("Balthazar"))

# Search for animals by language
print(forest.search_animal_by_language(lion_language))
print(forest.search_animal_by_language(giraffe_language))