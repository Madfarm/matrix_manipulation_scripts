import math

class Spacecraft:
    def __init__(self, mass, speed, x, y, fuel):
        self.mass = mass
        self.speed = speed
        self.x = x
        self.y = y
        self.fuel = fuel

    def course_correction(self, target_x, target_y):
        # Calculate the distance to the target
        distance = math.sqrt((target_x - self.x)**2 + (target_y - self.y)**2)

        # Calculate the gravitational force towards the target (Newton's law of universal gravitation)
        # For simplicity, we assume the target has a mass of 1 and the gravitational constant is 1
        force = self.mass * (1 / distance**2)

        # Calculate the acceleration needed to reach the target
        acceleration = force / (self.mass + self.fuel)

        # Calculate the course correction needed
        # For simplicity, we assume the target is in the positive x direction
        course_correction = math.atan(acceleration / self.speed)

        return course_correction

# Create a spacecraft
spacecraft = Spacecraft(1, 10, 0, 0, 100)

# Calculate the course correction to reach the target at (10, 10)
course_correction = spacecraft.course_correction(10, 10)

print(f"The course correction needed is {course_correction} radians.")