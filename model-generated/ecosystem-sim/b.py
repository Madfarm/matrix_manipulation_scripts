class Animal:
    def __init__(self, name, food_needed, water_needed, space_needed, population):
        self.name = name
        self.food_needed = food_needed
        self.water_needed = water_needed
        self.space_needed = space_needed
        self.population = population

    def eat(self):
        print(f'{self.name} is eating.')

    def drink(self):
        print(f'{self.name} is drinking.')

    def live(self):
        print(f'{self.name} is living.')

    def grow_population(self):
        self.population += 1
        print(f'{self.name} population increased.')


class Lion(Animal):
    def __init__(self):
        super().__init__('Lion', 10, 10, 100, 10)


class Gazelle(Animal):
    def __init__(self):
        super().__init__('Gazelle', 5, 5, 50, 100)


class Ostrich(Animal):
    def __init__(self):
        super().__init__('Ostrich', 3, 3, 30, 150)


lion = Lion()
gazelle = Gazelle()
ostrich = Ostrich()

lion.eat()
gazelle.drink()
ostrich.live()

lion.grow_population()
gazelle.grow_population()
ostrich.grow_population()

