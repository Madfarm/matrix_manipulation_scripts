def calculate_laundry_time(hot_load, wet_load, socks, underwear, shirts, pants, towels):
    # Define the time it takes for each item
    time_per_item = {
        'socks': 1,
        'underwear': 2,
        'shirts': 3,
        'pants': 3,
        'towels': 5
    }

    # Calculate the total time for each item
    total_time = sum([time_per_item[item] * count for item, count in zip(time_per_item.keys(), [socks, underwear, shirts, pants, towels])])

    # Add time for a hot load
    if hot_load:
        total_time *= 1.5

    # Add time for a wet load
    if wet_load:
        total_time += 20

    return total_time

# Test the function
hot_load = True
wet_load = True
socks = 5 # 5
underwear = 3 # 6
shirts = 2 # 6
pants = 1 # 3
towels = 0

total_time = calculate_laundry_time(hot_load, wet_load, socks, underwear, shirts, pants, towels)
print(f"The total time to fold the laundry is: {total_time} minutes")