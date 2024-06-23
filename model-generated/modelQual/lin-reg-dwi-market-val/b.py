import pandas as pd
import numpy as np

# Define the function
def linear_regression(percent_fatal_crashes_involving_alc, alc_market_val):
    # Store provided data in memory
    total_fatal_crashes = 39507
    data = {
        "Year": [2019, 2020, 2021, 2022],
        "Alcohol-Impaired Driving Fatalities": [10142, 11654, 13384, 13524],
        "Global Alcoholic Beverage Market (in billion USD)": [1450, 1500, 1730, 1800]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Add arguments to the dataset
    df.loc[4] = [2024, (percent_fatal_crashes_involving_alc * total_fatal_crashes), alc_market_val]

    # Perform linear regression
    slope, intercept = np.polyfit(data["Alcohol-Impaired Driving Fatalities"], data["Global Alcoholic Beverage Market (in billion USD)"], 1)
    
    # Print the results
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    
    # Check if there is a positive correlation
    if slope > 0:
        print("There is a positive correlation between alcohol-impaired driving fatalities and the global alcoholic beverage market.")
        return True
    else:
        print("There is no positive correlation between alcohol-impaired driving fatalities and the global alcoholic beverage market.")
        return False

# Call the function
linear_regression(.36, 1579)