# Define the data
plants = {
    'Tomato': {'growth': 24, 'water': 5, 'fertilizer': 7, 'equipment': 15},
    'Cucumber': {'growth': 18, 'water': 4, 'fertilizer': 6, 'equipment': 12},
    'Bell Pepper': {'growth': 20, 'water': 6, 'fertilizer': 8, 'equipment': 10},
    'Carrot': {'growth': 10, 'water': 3, 'fertilizer': 4, 'equipment': 8},
    'Lettuce': {'growth': 8, 'water': 2, 'fertilizer': 3, 'equipment': 5}
}

# Calculate the total cost for each plant
for plant, data in plants.items():
    total_cost = data['water'] + data['fertilizer'] + data['equipment']
    plants[plant]['total_cost'] = total_cost

# Calculate the cost per inch for each plant
for plant, data in plants.items():
    cost_per_inch = data['total_cost'] / data['growth']
    plants[plant]['cost_per_inch'] = cost_per_inch

# Find the most cost-efficient plant
most_cost_efficient_plant = min(plants, key=lambda x: plants[x]['cost_per_inch'])

# Print the results
print(f"The most cost-efficient plant is {most_cost_efficient_plant} with a cost per inch of ${plants[most_cost_efficient_plant]['cost_per_inch']:.2f}")
print(f"The total cost for {most_cost_efficient_plant} is ${plants[most_cost_efficient_plant]['total_cost']}")
