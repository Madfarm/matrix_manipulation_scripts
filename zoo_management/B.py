class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def makeSound(self):
        raise NotImplementedError("Subclasses should implement this method.")

class Lion(Animal):
    def makeSound(self):
        return "Roar!"

class Elephant(Animal):
    def makeSound(self):
        return "Trumpet!"

# Test the classes
lion = Lion("Leo")
elephant = Elephant("Ella")

lion.eat()
lion.sleep()
print(f"{lion.name} says {lion.makeSound()}")

elephant.eat()
elephant.sleep()
print(f"{elephant.name} says {elephant.makeSound()}")