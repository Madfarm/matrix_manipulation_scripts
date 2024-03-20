class Cheetah:
    def __init__(self, initial_speed):
        self.initial_speed = initial_speed

    def calculate_distance(self, time_in_seconds):
        if time_in_seconds <= 0:
            return 0
        elif time_in_seconds <= 5:
            return self.initial_speed * (1 + 0.1*time_in_seconds) * time_in_seconds / 2
        else:
            return self.initial_speed * (1 + 0.1*5) * 5 / 2 + \
                   self.initial_speed * (1 + 0.1*5) * (1 - 0.15*5) * (time_in_seconds - 5)

# Demonstration
cheetah = Cheetah(10) # initial speed of the cheetah is 10 m/s
print(cheetah.calculate_distance(10)) # prints the total distance covered in 10 seconds