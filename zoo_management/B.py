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
        sounds = []
        for animal in self.animals:
            sounds.append(animal.makeSound())
        return sounds

    def feed_animals(self):
        for animal in self.animals:
            print(animal.eat())

    def put_animals_to_sleep(self):
        for animal in self.animals:
            print(animal.sleep())

# Create a zoo and add some animals
my_zoo = Zoo()
my_zoo.add_animal(Elephant())
my_zoo.add_animal(Tiger())
my_zoo.add_animal(Horse())

# Make the animals make sounds
print(my_zoo.make_sounds())  # Output: ["Trumpet trumpet!", "Rrrrr...", "Neigh!"]

# Feed the animals
my_zoo.feed_animals()
# Output:
# Munch munch! *crunch crunch*
# Gobble gobble! *chomp chomp*
# Munch munch! *chomp chomp*

# Put the animals to sleep
my_zoo.put_animals_to_sleep()
# Output:
# Trumpet trumpet! *snore*
# Rrrrr... *yawn*
# Neigh... *whinny*