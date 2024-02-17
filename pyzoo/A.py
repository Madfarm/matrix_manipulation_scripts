class Animal:
    def __init__(self, name, age, gender, health_status, unique_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.health_status = health_status
        self.unique_id = unique_id

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_health_status(self):
        return self.health_status

    def get_unique_id(self):
        return self.unique_id

    def feed(self):
        print(f"Feeding {self.name}")

    def health_check(self):
        print(f"Checking health of {self.name}")

class Lion(Animal):
    def __init__(self, name, age, gender, health_status, unique_id):
        super().__init__(name, age, gender, health_status, unique_id)

class Zebra(Animal):
    def __init__(self, name, age, gender, health_status, unique_id):
        super().__init__(name, age, gender, health_status, unique_id)

class Giraffe(Animal):
    def __init__(self, name, age, gender, health_status, unique_id):
        super().__init__(name, age, gender, health_status, unique_id)

class Penguin(Animal):
    def __init__(self, name, age, gender, health_status, unique_id):
        super().__init__(name, age, gender, health_status, unique_id)

class Snake(Animal):
    def __init__(self, name, age, gender, health_status, unique_id):
        super().__init__(name, age, gender, health_status, unique_id)

def create_enclosure(animals):
    # Check if the animals can coexist in the same enclosure
    for animal in animals:
        if animal.get_name() == "Lion" or animal.get_name() == "Snake":
            # Predators should not be in the same enclosure as other animals
            return False
    return True

def daily_routine():
    animals = [
        Lion("Simba", 5, "Male", "Healthy", 1),
        Zebra("Stripes", 3, "Female", "Healthy", 2),
        Giraffe("Giggy", 7, "Male", "Healthy", 3),
        Penguin("Percy", 4, "Male", "Healthy", 4),
        Snake("Slinky", 6, "Female", "Healthy", 5)
    ]

    # Create enclosures
    enclosures = []
    for i in range(3):
        enclosures.append([])

    # Assign animals to enclosures
    for animal in animals:
        found_enclosure = False
        for enclosure in enclosures:
            if create_enclosure(enclosure + [animal]):
                enclosure.append(animal)
                found_enclosure = True
                break
        if not found_enclosure:
            print(f"Error: Could not find suitable enclosure for {animal.get_name()}")

    # Perform daily routine
    for enclosure in enclosures:
        for animal in enclosure:
            animal.feed()
            animal.health_check()

daily_routine()