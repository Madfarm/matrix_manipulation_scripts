class Animal:
    def __init__(self, age):
        self.hasBeenFed = False
        self.hasSlept = False
        self.age = age

    def sleep(self):
        self.hasSlept = True
        return "Zzz..."

    def eat(self):
        if self.hasBeenFed:
            return "Munch munch! *burp*"
        else:
            return "Munch munch! *hungry*"

    def makeSound(self):
        if self.age < 2:
            return "Squeak squeak!"
        else:
            return "..."

class Elephant(Animal):
    def __init__(self, age):
        super().__init__(age)

    def sleep(self):
        self.hasSlept = True
        return "Trumpet trumpet! *snore*"

    def eat(self):
        if self.hasBeenFed:
            return "Munch munch! *crunch crunch* *burp*"
        else:
            return "Munch munch! *crunch crunch* *hungry*"

    def makeSound(self):
        if self.age < 2:
            return "Squeak squeak! *trumpet*"
        else:
            return "Trumpet trumpet!"

class Tiger(Animal):
    def __init__(self, age):
        super().__init__(age)

    def sleep(self):
        self.hasSlept = True
        return "Rrrrr... *yawn*"

    def eat(self):
        if self.hasBeenFed:
            return "Gobble gobble! *chomp chomp* *burp*"
        else:
            return "Gobble gobble! *chomp chomp* *hungry*"

    def makeSound(self):
        if self.age < 2:
            return "Squeak squeak! *growl*"
        else:
            return "Rrrrr..."

class Horse(Animal):
    def __init__(self, age):
        super().__init__(age)

    def sleep(self):
        self.hasSlept = True
        return "Neigh... *whinny*"

    def eat(self):
        if self.hasBeenFed:
            return "Munch munch! *chomp chomp* *burp*"
        else:
            return "Munch munch! *chomp chomp* *hungry*"

    def makeSound(self):
        if self.age < 2:
            return "Squeak squeak! *neigh*"
        else:
            return "Neigh!"

class Zoo:
    def __init__(self):
        self.animals = []
        self.num_animals = 0
        self.num_unfed_animals = 0
        self.num_young_animals = 0

    def add_animal(self, animal):
        self.animals.append(animal)
        self.num_animals += 1
        if animal.age < 2:
            self.num_young_animals += 1

    def feed_animals(self):
        for animal in self.animals:
            animal.hasBeenFed = True
            print(animal.eat())

    def make_sounds(self):
        for animal in self.animals:
            print(animal.makeSound())

    def get_num_animals(self):
        return self.num_animals

    def get_num_unfed_animals(self):
        return self.num_unfed_animals

    def get_num_young_animals(self):
        return self.num_young_animals

# Create a zoo with some animals
zoo = Zoo()
zoo.add_animal(Elephant(1))
zoo.add_animal(Tiger(3))
zoo.add_animal(Horse(2))

# Test the zoo methods
print("Making sounds:")
zoo.make_sounds()
print("\nFeeding animals:")
zoo.feed_animals()
print("\nNumber of animals:", zoo.get_num_animals())
print("Number of unfed animals:", zoo.get_num_unfed_animals())
print("Number of young animals (less than 2 years old):", zoo.get_num_young_animals())