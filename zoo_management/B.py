class Animal:
    def __init__(self, name):
        self.name = name
    
    def sleep(self):
        return "Zzz..."
    
    def eat(self):
        return "Munch munch!"

class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def sleep(self):
        return "Trumpet trumpet! *snore*"
    
    def eat(self):
        return "Munching on some tasty leaves!"
    
    def makeSound(self):
        return "Trumpet trumpet!"

class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def sleep(self):
        return "Rrrrr... *yawn*"
    
    def eat(self):
        return "Crunching on some fresh meat!"
    
    def makeSound(self):
        return "Rrrrr..."

class Horse(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def sleep(self):
        return "Neigh... *snore*"
    
    def eat(self):
        return "Munching on some juicy hay!"
    
    def makeSound(self):
        return "Neigh!"

# Create some animals
my_elephant = Elephant("Babar")
my_tiger = Tiger("Shere Khan")
my_horse = Horse("Black Beauty")

# Test the methods
print(my_elephant.sleep())  # Trumpet trumpet! *snore*
print(my_tiger.eat())  # Crunching on some fresh meat!
print(my_horse.makeSound())  # Neigh!