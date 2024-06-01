import pandas as pd

# Create a DataFrame from the table
df = pd.DataFrame({
    'Plant': ['Tomato', 'Cucumber', 'Bell Pepper', 'Carrot', 'Lettuce'],
    'Growth (inches)': [24, 18, 20, 10, 8],
    'Cost of Water': [5, 4, 6, 3, 2],
    'Cost of Fertilizer': [7, 6, 8, 4, 3],
    'Cost of Equipment': [15, 12, 10, 8, 5]
})

# Calculate the total cost for each plant
df['Total Cost'] = df['Cost of Water'] + df['Cost of Fertilizer'] + df['Cost of Equipment']

# Calculate the cost per inch for each plant
df['Cost per Inch'] = df['Total Cost'] / df['Growth (inches)']

# Find the most cost-efficient plant
most_efficient_plant = df.loc[df['Cost per Inch'].idxmin()]

# Print the results
print(f"The most cost-efficient plant is {most_efficient_plant['Plant']} with a cost per inch of ${most_efficient_plant['Cost per Inch']:.2f}.")
print(f"The total cost for this plant is ${most_efficient_plant['Total Cost']:.2f}.")
