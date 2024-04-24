from decimal import Decimal


class Particle:
    def __init__(self, mass, position, velocity):
        self.mass = Decimal(mass)
        self.position = Decimal(position)
        self.velocity = Decimal(velocity)


    def update_position(self, time_elapsed):
        self.position += self.velocity * Decimal(time_elapsed)


def calculate_total_momentum(particles):
    total_momentum = Decimal(0)
    for particle in particles:
        total_momentum += particle.mass * particle.velocity
    return total_momentum


# Create particles
particle1 = Particle(1.0, 0.0, 1.0)
particle2 = Particle(2.0, 0.0, 2.0)


# Update positions
particle1.update_position(1.0)
particle2.update_position(1.0)


# Assert position updates
assert particle1.position == Decimal(1.0), "Position update for particle 1 is incorrect"
assert particle2.position == Decimal(2.0), "Position update for particle 2 is incorrect"


# Calculate total momentum
total_momentum = calculate_total_momentum([particle1, particle2])


# Assert momentum calculation
assert total_momentum == Decimal(5.0), "Total momentum calculation is incorrect"

