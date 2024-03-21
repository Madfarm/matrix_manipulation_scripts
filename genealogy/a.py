class Animal:
    def __init__(self, category, family, genus, name, id):
        self.category = category
        self.family = family
        self.genus = genus
        self.name = name
        self.id = id

class FamilyTree:
    def __init__(self):
        self.tree = {}

    def add_relation(self, child, parent1, parent2=None):
        if child in self.tree:
            print("Child already exists in the tree.")
            return
        self.tree[child] = [parent1, parent2]

    def search(self, id=None, name=None):
        if id is not None:
            for animal, details in self.tree.items():
                if details[0] == id or details[1] == id:
                    return animal
        elif name:
            for animal, details in self.tree.items():
                if details[0] == name or details[1] == name:
                    return animal
        return None

# Adding animals
dog = Animal('Mammal', 'Canidae', 'Canis', 'Dog', 'D001')
cat = Animal('Mammal', 'Felidae', 'Felis', 'Cat', 'C001')
lion = Animal('Mammal', 'Felidae', 'Panthera', 'Lion', 'L001')

# Creating Family Tree
ft = FamilyTree()
ft.add_relation(dog, cat, lion)
print(ft.tree.keys())

# Searching
print(ft.search(id='L001'))  # Output: Animal object for Lion
print(ft.search(name='Cat'))  # Output: Animal object for Cat