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
        # For simplicity, assume the target has a mass of 1 and the gravitational constant is 1
        force = self.mass * (1 / distance**2)

        # Calculate the angle of the force vector
        angle = math.atan2(target_y - self.y, target_x - self.x)

        # Calculate the correction needed in the x and y directions
        correction_x = force * math.cos(angle)
        correction_y = force * math.sin(angle)

        return correction_x, correction_y

# Create a spacecraft
craft = Spacecraft(1, 0, 0, 0, 100)

# Calculate the course correction to the target at (5, 5)
correction_x, correction_y = craft.course_correction(5, 5)

print(f"Course correction needed: {correction_x} in the x direction, {correction_y} in the y direction")