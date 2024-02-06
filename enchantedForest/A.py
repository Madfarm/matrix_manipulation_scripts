class Animal:
    def __init__(self, name, species, habitat):
        self.name = name
        self.species = species
        self.habitat = habitat

    def __str__(self):
        return f"{self.name} ({self.species}) - Habitat: {self.habitat}"

class Bird(Animal):
    def __init__(self, name, species, habitat, wingspan):
        super().__init__(name, species, habitat)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} spreads its wings and takes flight!")

    def __str__(self):
        return super().__str__() + f", Wingspan: {self.wingspan}"

class Mammal(Animal):
    def __init__(self, name, species, habitat, num_legs):
        super().__init__(name, species, habitat)
        self.num_legs = num_legs

    def run(self):
        print(f"{self.name} gallops away on its {self.num_legs} legs!")

class EnchantedAnimal(Animal):
    def __init__(self, name, species, habitat, magical_ability):
        super().__init__(name, species, habitat)
        self.magical_ability = magical_ability

    def perform_magic(self):
        print(f"{self.name} uses its {self.magical_ability}!")

    def __str__(self):
        return super().__str__() + f", Magical Ability: {self.magical_ability}"

class Forest:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                self.animals.remove(animal)
                print(f"{name} has been removed from the forest.")
                return
        print(f"{name} not found in the forest.")

    def display_animals(self):
        if not self.animals:
            print("The forest is currently empty.")
        else:
            for animal in self.animals:
                print(animal)

    def find_by_name(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal
        return None

    def find_by_species(self, species):
        return [animal for animal in self.animals if animal.species == species]

    def find_by_magical_ability(self, ability):
        return [animal for animal in self.animals if isinstance(animal, EnchantedAnimal) and animal.magical_ability == ability]

# Create the forest
forest = Forest()

# Add some animals
forest.add_animal(Bird("Flit", "Hummingbird", "Flower meadow", "0.5 ft"))
forest.add_animal(Mammal("Dash", "Deer", "Woodland", 4))
forest.add_animal(EnchantedAnimal("Sparkle", "Unicorn", "Glade of Dreams", "Healing"))
forest.add_animal(EnchantedAnimal("Willow", "Wisp", "Misty Swamp", "Invisibility"))

# Interact with the forest
while True:
    print("\nWhat would you like to do?")
    print("1. Add an animal")
    print("2. Remove an animal")
    print("3. Display all animals")
    print("4. Find animal by name")
    print("5. Find animals by species")
    print("6. Find animals by magical ability")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # ... (add animal logic here)
        pass
    elif choice == "2":
        # ... (remove animal logic here)
        pass
    elif choice == "3":
        forest.display_animals()
    elif choice == "4":
        # ... (find by name logic here)
        pass
    elif choice == "5":
        # ... (find by species logic here)
        pass
    elif choice == "6":
        # ... (find by magical ability logic here)
        pass
    elif choice == "7":
        break
    else:
        print("Invalid choice.")