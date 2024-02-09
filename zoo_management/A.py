class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def makeSound(self):
        print(f"{self.name} makes a generic animal sound.")

class Lion(Animal):
    def makeSound(self):
        print("Roar!")

class Elephant(Animal):
    def makeSound(self):
        print("Trumpet!")

lion = Lion("Leo", 5)
elephant = Elephant("Ellie", 10)

lion.makeSound()  # Output: Roar!
elephant.makeSound()  # Output: Trumpet!