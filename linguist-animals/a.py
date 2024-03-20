class Animal:
    def __init__(self, name, species, language):
        self.name = name
        self.species = species
        self.language = language

class Language:
    def __init__(self, name, characters, grammar_rules):
        self.name = name
        self.characters = characters
        self.grammar_rules = grammar_rules

class Linguist:
    def __init__(self):
        self.animals = []

    def add_animal(self, name, species, language):
        self.animals.append(Animal(name, species, language))

    def update_animal(self, name, new_name=None, new_species=None, new_language=None):
        for animal in self.animals:
            if animal.name == name:
                if new_name:
                    animal.name = new_name
                if new_species:
                    animal.species = new_species
                if new_language:
                    animal.language = new_language

    def search_animal(self, name=None, language=None):
        if name:
            return [animal for animal in self.animals if animal.name == name]
        elif language:
            return [animal for animal in self.animals if animal.language == language]

# create linguist
linguist = Linguist()

# create languages
english = Language('English', 'abcdefghijklmnopqrstuvwxyz', 'Subject-Verb-Object')
french = Language('French', 'abcdefghijklmnopqrstuvwxyzéàèù', 'Verb-Subject-Object')

# add animals
linguist.add_animal('John', 'Human', english)
linguist.add_animal('Fifi', 'French bulldog', french)

# update animal
linguist.update_animal('Fifi', new_species='Bulldog')

# search animals
print(linguist.search_animal(name='John'))  # returns [Animal object for John]
print(linguist.search_animal(language=french))  # returns [Animal object for Fifi]