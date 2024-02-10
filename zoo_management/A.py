class Animal:
    def __init__(self):
        self.hasBeenFed = False

    def sleep(self):
        return "Zzz..."

    def eat(self):
        if self.hasBeenFed:
            return "Munch munch! *burp*"
        else:
            return "Munch munch! *hungry*"

    def makeSound(self):
        return "..."

class Elephant(Animal):
    def sleep(self):
        return "Trumpet trumpet! *snore*"

    def eat(self):
        if self.hasBeenFed:
            return "Munch munch! *crunch crunch* *burp*"
        else:
            return "Munch munch! *crunch crunch* *hungry*"

    def makeSound(self):
        return "Trumpet trumpet!"

class Tiger(Animal):
    def sleep(self):
        return "Rrrrr... *yawn*"

    def eat(self):
        if self.hasBeenFed:
            return "Gobble gobble! *chomp chomp* *burp*"
        else:
            return "Gobble gobble! *chomp chomp* *hungry*"

    def makeSound(self):
        return "Rrrrr..."

class Horse(Animal):
    def sleep(self):
        return "Neigh... *whinny*"

    def eat(self):
        if self.hasBeenFed:
            return "Munch munch! *chomp chomp* *burp*"
        else:
            return "Munch munch! *chomp chomp* *hungry*"

    def makeSound(self):
        return "Neigh!"

class Zoo:
    def __init__(self):
        self.animals = []
        self.num_animals = 0
        self.num_unfed_animals = 0

    def add_animal(self, animal):
        self.animals.append(animal)
        self.num_animals += 1

    def feed_animals(self):
        for animal in self.animals:
            animal.hasBeenFed = True
            print(animal.eat())

    def make_sounds(self):
        for animal in self.animals:
            print(animal.makeSound())

    def get_num_unfed_animals(self):
        return self.num_unfed_animals

    def get_num_animals(self):
        return self.num_animals

# Create a zoo with some animals
zoo = Zoo()
zoo.add_animal(Elephant())
zoo.add_animal(Tiger())
zoo.add_animal(Horse())

# Feed the animals
zoo.feed_animals()

# Print the number of unfed animals
print("Number of unfed animals:", zoo.get_num_unfed_animals())

# Print the number of animals
print("Number of animals:", zoo.get_num_animals())