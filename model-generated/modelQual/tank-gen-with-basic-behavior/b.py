import random

class Tank:
    def __init__(self):
        self.health = random.randint(1, 500)
        self.speed = random.randint(10, 100)
        self.range = random.randint(1, 4)
        self.damage = random.randint(50, 100)
        self.position = 0
        self.firepower = random.randint(50, 100)
        self.protection = random.randint(50, 100)
        self.mobility = random.randint(50, 100)
        self.active_protection_system = True

    def move(self, direction):
        if direction == 'left':
            self.position -= self.speed
        elif direction == 'right':
            self.position += self.speed
        else:
            print("Invalid direction. Please enter 'left' or 'right'.")

# Generate a tank
tank = Tank()
print("Tank's initial position:", tank.position)

# Move the tank
tank.move('right')
print("Tank's position after moving right:", tank.position)

tank.move('left')
print("Tank's position after moving left:", tank.position)