import random

# Penguin class to store identifier, hunger level, and feeding history
class Penguin:
    def __init__(self, id):
        self.id = id
        self.hunger = 0
        self.feeding_history = []

# Initialize penguins
penguins = [Penguin(i) for i in range(10)]

# Emperor Penguin
emperor_penguin = Penguin("Emperor")

# Feeding queue
queue = []

# Simulation parameters
hunger_threshold = 5  # penguins get hungry every 5 turns
impatience_probability = 0.2  # 20% chance a penguin gets impatient
double_eat_probability = 0.1  # 10% chance a penguin eats twice in a row

# Simulation loop
for turn in range(100):
    # Penguins get hungry
    for penguin in penguins:
        if penguin.hunger >= hunger_threshold:
            penguin.hunger = 0
            queue.append(penguin)
    
    # Penguins join or leave the queue randomly
    for _ in range(random.randint(0, 2)):
        penguin = random.choice(penguins)
        if random.random() < 0.5:  # 50% chance to join or leave queue
            queue.append(penguin)
        else:
            queue.remove(penguin)
    
    # Penguins get impatient and skip a turn
    for penguin in queue:
        if random.random() < impatience_probability:
            queue.remove(penguin)
            penguin.hunger += 1
    
    # Penguins eat twice in a row
    for penguin in queue:
        if random.random() < double_eat_probability:
            penguin.feeding_history.append(turn)
            penguin.hunger = 0
            queue.remove(penguin)
            if penguin.id == emperor_penguin.id:  # Emperor Penguin eats twice
                penguin.feeding_history.append(turn)
    
    # Feed penguins in the queue
    for penguin in queue:
        penguin.feeding_history.append(turn)
        penguin.hunger = 0
        queue.remove(penguin)
    
    # Record which penguin ate the most
    max_eater = max(penguins, key=lambda p: len(p.feeding_history))
    print(f"Turn {turn+1}: Penguin {max_eater.id} ate the most ({len(max_eater.feeding_history)} times)")

# Print the feeding history of each penguin
for penguin in penguins:
    print(f"Penguin {penguin.id} ate {len(penguin.feeding_history)} times")

# Print the Emperor Penguin's feeding history
print(f"Emperor Penguin ate {len(emperor_penguin.feeding_history)} times")