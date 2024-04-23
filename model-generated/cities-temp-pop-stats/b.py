import pandas as pd
from scipy import stats


# Create a DataFrame from the given data
data = {
    "City": ["New York City, NY", "Los Angeles, CA", "Chicago, IL", "Houston, TX", "Phoenix, AZ"],
    "Population (Est. 2023)": [8804190, 3971883, 2746388, 2325502, 1680915],
    "Average High Temp. (August)": [82, 88, 83, 95, 105],
    "Major Industry": ["Finance, Media, Technology", "Entertainment, Media, Manufacturing", "Finance, Manufacturing, Transportation", "Energy, Healthcare, Manufacturing", "Tourism, Healthcare, Construction"]
}
df = pd.DataFrame(data)


# Remove cities with population above 5 million
df = df[df["Population (Est. 2023)"] <= 5000000]


# Remove cities with Fishing as a major industry
df = df[~df["Major Industry"].str.contains("Fishing")]


# Calculate mean, median, and standard deviation for population and temperature
population_stats = {
    "mean": stats.tmean(df["Population (Est. 2023)"]),
    "median": stats.median(df["Population (Est. 2023)"]),
    "std_dev": stats.tstd(df["Population (Est. 2023)"])
}


temperature_stats = {
    "mean": stats.tmean(df["Average High Temp. (August)"]),
    "median": stats.tmedian(df["Average High Temp. (August)"]),
    "std_dev": stats.tstd(df["Average High Temp. (August)"])
}


# Store the results in a dictionary
stats_dict = {
    "population": population_stats,
    "temperature": temperature_stats
}


# Validate the dictionary and calculations using assertions
assert isinstance(stats_dict, dict), "stats_dict is not a dictionary"
assert len(stats_dict) == 2, "stats_dict does not contain two keys"
assert "population" in stats_dict, "stats_dict does not contain 'population' key"
assert "temperature" in stats_dict, "stats_dict does not contain 'temperature' key"


for key in stats_dict:
    assert isinstance(stats_dict[key], dict), f"stats_dict['{key}'] is not a dictionary"
    assert len(stats_dict[key]) == 3, f"stats_dict['{key}'] does not contain three keys"
    assert "mean" in stats_dict[key], f"stats_dict['{key}'] does not contain 'mean' key"
    assert "median" in stats_dict[key], f"stats_dict['{key}'] does not contain 'median' key"
    assert "std_dev" in stats_dict[key], f"stats_dict['{key}'] does not contain 'std_dev' key"


print(stats_dict)