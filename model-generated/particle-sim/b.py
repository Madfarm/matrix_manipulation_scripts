from decimal import Decimal


class Particle:
    def __init__(self, mass, position, velocity):
        self.mass = Decimal(mass)
        self.position = Decimal(position)
        self.velocity = Decimal(velocity)


    def update_position(self, time_elapsed):
        self.position += self.velocity * Decimal(time_elapsed)


    def get_momentum(self):
        return self.mass * self.velocity


def calculate_total_momentum(particles):
    total_momentum = Decimal(0)
    for particle in particles:
        total_momentum += particle.get_momentum()
    return total_momentum


# Create a list of particles
particles = [
    Particle(1, 0, 1),
    Particle(2, 1, 2),
    Particle(3, 2, 3)
]


# Update positions and calculate total momentum
time_elapsed = Decimal(1)
for particle in particles:
    particle.update_position(time_elapsed)


total_momentum = calculate_total_momentum(particles)


# Print the updated positions and total momentum
for i, particle in enumerate(particles):
    print(f'Particle {i+1} position: {particle.position}')
print(f'Total momentum: {total_momentum}')