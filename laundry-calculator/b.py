def calculate_folding_time(load, temperature):
    # Define the time it takes to fold each item
    folding_times = {
        "socks": 1,
        "underwear": 2,
        "shirts": 3,
        "pants": 3,
        "towels": 5
    }

    # Initialize the total folding time
    total_time = 0

    # Calculate the folding time for each item in the load
    for item, quantity in load.items():
        if item in folding_times:
            total_time += folding_times[item] * quantity

    # Adjust the folding time based on the temperature
    if temperature == "hot":
        total_time *= 1.5
    elif temperature == "wet":
        total_time += 20

    return total_time

# Define the load
load = {
    "socks": 5, # 5
    "underwear": 3, # 6
    "shirts": 2, # 6
    "pants": 2, # 6
    "towels": 1 # 5
}

# Define the temperature
temperature = "hot"

# Calculate the folding time
folding_time = calculate_folding_time(load, temperature)

# Print the result
print(f"It will take {folding_time} minutes to fold the load.")