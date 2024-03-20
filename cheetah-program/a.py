class Cheetah:
    def __init__(self, initial_speed):
        self.initial_speed = initial_speed

    def calculate_distance(self, seconds):
        total_distance = 0
        speed = self.initial_speed

        for i in range(seconds):
            if i < 5:
                speed *= 1.1  # Increase speed by 10%
            else:
                speed *= 0.85  # Decrease speed by 15%

            total_distance += speed

        return total_distance

# Create a new Cheetah with an initial speed of 50 mph
cheetah = Cheetah(50)

# Calculate the distance covered within 10 seconds
distance = cheetah.calculate_distance(10)
print(f"The cheetah covered {distance} meters in 10 seconds.")

