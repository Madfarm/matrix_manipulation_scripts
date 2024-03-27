class Ecosystem:
    def __init__(self):
        self.species = []

    def add_species(self, species):
        self.species.append(species)

    def simulate(self):
        for s in self.species:
            s.update()
        for s in self.species:
            for other in self.species:
                if other != s:
                    s.interact(other)

class Species:
    def __init__(self, name, food_needed, water_needed, space_needed, population):
        self.name = name
        self.food_needed = food_needed
        self.water_needed = water_needed
        self.space_needed = space_needed
        self.population = population
        self.food = 0
        self.water = 0
        self.space = 0

    def update(self):
        # Grow population
        self.population *= 1.1

        # Consume resources
        self.food -= self.food_needed * self.population
        self.water -= self.water_needed * self.population
        self.space -= self.space_needed * self.population

    def interact(self, other):
        if self.space > other.space:
            self.population += other.population * 0.1
            other.population -= other.population * 0.1

lion = Species("Lion", 10, 10, 100, 100)
zebra = Species("Zebra", 5, 5, 50, 1000)
waterhole = Ecosystem()
waterhole.add_species(lion)
waterhole.add_species(zebra)

for i in range(10):
    waterhole.simulate()
    print("Lion Population:", lion.population)
    print("Zebra Population:", zebra.population)
    print("---")