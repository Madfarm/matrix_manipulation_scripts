class Animal:
    def __init__(self, name, age, gender, health_status, id):
        self.name = name
        self.age = age
        self.gender = gender
        self.health_status = health_status
        self.id = id

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_health_status(self):
        return self.health_status

    def get_id(self):
        return self.id

class Lion(Animal):
    def __init__(self, name, age, gender, health_status, id):
        super().__init__(name, age, gender, health_status, id)

class Zebra(Animal):
    def __init__(self, name, age, gender, health_status, id):
        super().__init__(name, age, gender, health_status, id)

class Giraffe(Animal):
    def __init__(self, name, age, gender, health_status, id):
        super().__init__(name, age, gender, health_status, id)

class Penguin(Animal):
    def __init__(self, name, age, gender, health_status, id):
        super().__init__(name, age, gender, health_status, id)

class Snake(Animal):
    def __init__(self, name, age, gender, health_status, id):
        super().__init__(name, age, gender, health_status, id)

def is_compatible(animal1, animal2):
    # predators and preys should not be in the same enclosure
    if animal1.get_id() in [Lion.id, Snake.id] and animal2.get_id() in [Zebra.id, Giraffe.id, Penguin.id]:
        return False
    elif animal2.get_id() in [Lion.id, Snake.id] and animal1.get_id() in [Zebra.id, Giraffe.id, Penguin.id]:
        return False
    else:
        return True

def daily_feeding(animals):
    for animal in animals:
        print(f"Feeding {animal.get_name()}")

def health_check_up(animals):
    for animal in animals:
        print(f"Checking health of {animal.get_name()}")

def visiting_hours(animals):
    for animal in animals:
        print(f"Visiting {animal.get_name()}")

def create_enclosure(animals):
    enclosure = []
    for animal in animals:
        if not is_compatible(animal, enclosure):
            raise ValueError("Incompatible animals")
        enclosure.append(animal)
    return enclosure

# create some animals
lion1 = Lion("Simba", 3, "male", "healthy", 1)
zebra1 = Zebra("Stripes", 5, "female", "healthy", 2)
giraffe1 = Giraffe("Gerald", 7, "male", "healthy", 3)
penguin1 = Penguin("Percy", 2, "male", "healthy", 4)
snake1 = Snake("Slinky", 4, "male", "healthy", 5)

# create an enclosure
enclosure = create_enclosure([lion1, zebra1, giraffe1, penguin1])

# daily feeding
daily_feeding(enclosure)

# health check-up
health_check_up(enclosure)

# visiting hours
visiting_hours(enclosure)