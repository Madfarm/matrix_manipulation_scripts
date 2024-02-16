import random

# Define the penguins and their identifiers
penguins = {"Penny": 0, "Percy": 1, "Pete": 2, "Paula": 3, "Pierre": 4, "Emperor": 5}
meal_counts = {penguin: 0 for penguin in penguins}  # Initialize meal counts to

# Define the meal counter and the most-fed penguin
meals_served = 0
most_fed_penguin = None

while meals_served < 100:  # Simulate 100 meals
    # Randomly select a penguin to join or leave the queue
    penguin_id = random.choice(list(penguins.keys()))
    if random.random() < 0.5:  # 50% chance to join the queue
        penguins[penguin_id] += 1  # Increment the penguin's queue position
    else:  # 50% chance to leave the queue
        penguins[penguin_id] -= 1  # Decrement the penguin's queue position
        if penguins[penguin_id] < 0:  # If the penguin leaves the queue, set its position to 0
            penguins[penguin_id] = 0

    # Serve meals to the penguins in the queue
    for penguin in penguins:
        if penguins[penguin] > 0:  # If the penguin is in the queue
            meal_counts[penguin] += 1  # Increment the meal count for the penguin
            if penguin == "Emperor":  # Emperor Penguin eats last and twice
                meals_served += 2
                penguins["Emperor"] += 2
                # Ensure the Emperor Penguin eats last
                for other_penguin in penguins:
                    if other_penguin != "Emperor" and penguins[other_penguin] > 0:
                        penguins[other_penguin] -= 1  # Decrement the other penguin's queue position
            else:
                # Serve a meal to the penguin
                meals_served += 1
                penguins[penguin] -= 1  # Decrement the penguin's queue position

    # Identify the most-fed penguin
    if most_fed_penguin is None or penguins[penguin] > penguins[most_fed_penguin]:
        most_fed_penguin = penguin

print("Meals served:", meals_served)
print("Most-fed penguin:", most_fed_penguin)
print("Number of meals eaten by the most-fed penguin:", penguins[most_fed_penguin])

# Print the number of meals each penguin ate
for penguin, meals in meal_counts.items():
    print(f"{penguin}: {meals} meals")