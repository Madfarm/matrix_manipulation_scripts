class Animal:
    def sleep(self):
        return "Zzz..."

    def eat(self):
        return "Munch munch!"

class Elephant(Animal):
    def sleep(self):
        return "Trumpet trumpet! *snore*"

    def eat(self):
        return "Munch munch! *crunch crunch*"

    def makeSound(self):
        return "Trumpet trumpet!"

class Tiger(Animal):
    def sleep(self):
        return "Rrrrr... *yawn*"

    def eat(self):
        return "Gobble gobble! *chomp chomp*"

    def makeSound(self):
        return "Rrrrr..."

class Horse(Animal):
    def sleep(self):
        return "Neigh... *whinny*"

    def eat(self):
        return "Munch munch! *chomp chomp*"

    def makeSound(self):
        return "Neigh!"

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def make_sounds(self):
        for animal in self.animals:
            print(animal.makeSound())

    def feed_animals(self):
        for animal in self.animals:
            print(animal.eat())

    def put_animals_to_sleep(self):
        for animal in self.animals:
            print(animal.sleep())

# Create a zoo with some animals
zoo = Zoo()
zoo.add_animal(Elephant())
zoo.add_animal(Tiger())
zoo.add_animal(Horse())

# Test the zoo methods
print("Making sounds:")
zoo.make_sounds()
print("\nFeeding animals:")
zoo.feed_animals()
print("\nPutting animals to sleep:")
zoo.put_animals_to_sleep()