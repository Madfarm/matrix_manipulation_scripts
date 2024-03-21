class Animal:
    def __init__(self, category, family, genus, name, id):
        self.category = category
        self.family = family
        self.genus = genus
        self.name = name
        self.id = id

    def __str__(self):
        return f"{self.name} ({self.id})"


class FamilyTree:
    def __init__(self):
        self.animals = {}

    def add_animal(self, animal):
        self.animals[animal.id] = animal

    def get_animal(self, id):
        return self.animals.get(id)

    def search(self, term):
        if isinstance(term, int):
            return self.get_animal(term)
        elif isinstance(term, str):
            for animal in self.animals.values():
                if animal.name == term:
                    return animal
        return None

    def print_family_tree(self, id):
        if id not in self.animals:
            return
        animal = self.animals[id]
        print(f"{animal.name} ({animal.id})")
        children = [child for child in self.animals.values() if child.genus == animal.genus]
        for child in children:
            print(f"  {child.name} ({child.id})")


# Example usage
tree = FamilyTree()

# Add animals
tree.add_animal(Animal("Mammalia", "Canidae", "Canis", "Dog", 1))
tree.add_animal(Animal("Mammalia", "Felidae", "Felis", "Cat", 2))
tree.add_animal(Animal("Mammalia", "Canidae", "Canis", "Wolf", 3))
tree.add_animal(Animal("Mammalia", "Felidae", "Panthera", "Lion", 4))
tree.add_animal(Animal("Mammalia", "Felidae", "Panthera", "Tiger", 5))

# Search for an animal
print(tree.search(1))  # Search by ID
print(tree.search("Cat"))  # Search by name


print("asdasd")

# Print family tree
tree.print_family_tree(5)  # Print the family tree of Cat