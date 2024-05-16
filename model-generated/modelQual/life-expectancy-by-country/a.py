import pandas as pd

def calculate_life_expectancy(data):
    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Group by country and calculate mean age
    means = df.groupby('country')['age'].mean()

    # Convert the result to a dictionary
    life_expectancy = means.to_dict()

    return life_expectancy

# Example usage:
data = [
    {'name': 'John', 'country': 'USA', 'age': 75},
    {'name': 'Jane', 'country': 'Canada', 'age': 80},
    {'name': 'Bob', 'country': 'USA', 'age': 70},
    {'name': 'Alice', 'country': 'Canada', 'age': 85},
    # Add more data here...
]

life_expectancy = calculate_life_expectancy(data)
print(life_expectancy)