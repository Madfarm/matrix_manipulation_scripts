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

# Test the classes
my_elephant = Elephant()
print(my_elephant.sleep())  # Output: Trumpet trumpet! *snore*
print(my_elephant.eat())  # Output: Munch munch! *crunch crunch*
print(my_elephant.makeSound())  # Output: Trumpet trumpet!

my_tiger = Tiger()
print(my_tiger.sleep())  # Output: Rrrrr... *yawn*
print(my_tiger.eat())  # Output: Gobble gobble! *chomp chomp*
print(my_tiger.makeSound())  # Output: Rrrrr...

my_horse = Horse()
print(my_horse.sleep())  # Output: Neigh... *whinny*
print(my_horse.eat())  # Output: Munch munch! *chomp chomp*
print(my_horse.makeSound())  # Output: Neigh!