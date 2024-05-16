import pandas as pd

def calculate_life_expectancy(data):
    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Group by country and calculate mean age
    life_expectancy = df.groupby('country')['age'].mean().to_dict()

    return life_expectancy

# Example usage:
data = [
    {'name': 'John', 'country': 'USA', 'age': 70},
    {'name': 'Jane', 'country': 'Canada', 'age': 65},
    {'name': 'Bob', 'country': 'USA', 'age': 75},
    {'name': 'Alice', 'country': 'Canada', 'age': 60},
    {'name': 'Mike', 'country': 'Mexico', 'age': 68},
    {'name': 'Sarah', 'country': 'Mexico', 'age': 72},
]

print(calculate_life_expectancy(data))