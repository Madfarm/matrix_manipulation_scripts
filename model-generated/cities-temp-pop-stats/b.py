import pandas as pd
from scipy import stats


def process_data(data):
    # Remove cities with population above 5 million
    data = data[data['Population (Est. 2023)'] <= 5000000]


    # Remove cities with Fishing as a major industry
    data = data[~data['Major Industry'].str.contains('Fishing')]


    # Calculate mean, median, and standard deviation for population and temperature
    population_stats = {
        'mean': stats.tmean(data['Population (Est. 2023)']),
        'median': data['Population (Est. 2023)'].median(),
        'std_dev': stats.tstd(data['Population (Est. 2023)']),
        'mad': stats.median_abs_deviation(data['Population (Est. 2023)'])
    }


    temperature_stats = {
        'mean': stats.tmean(data['Average High Temp. (August)']),
        'median': data['Average High Temp. (August)'].median(),
        'std_dev': stats.tstd(data['Average High Temp. (August)']),
        'mad': stats.median_abs_deviation(data['Average High Temp. (August)'])
    }


    # Store the results in a dictionary
    result = {
        'population': population_stats,
        'temperature': temperature_stats
    }


    return result


# Load the data
data = pd.DataFrame({
    'City': ['New York City, NY', 'Los Angeles, CA', 'Chicago, IL', 'Houston, TX', 'Phoenix, AZ'],
    'Population (Est. 2023)': [8804190, 3971883, 2746388, 2325502, 1680915],
    'Average High Temp. (August)': [82, 88, 83, 95, 105],
    'Major Industry': ['Finance, Media, Technology', 'Entertainment, Media, Manufacturing', 'Finance, Manufacturing, Transportation', 'Energy, Healthcare, Manufacturing', 'Tourism, Healthcare, Construction']
})


# Process the data
result = process_data(data)

# Validate the results
assert result['population']['mean'] == 2681172.0
assert result['population']['median'] == 2535945.0
assert result['population']['std_dev'] == 965609.1733764063
assert result['population']['mad'] == 532736.5


assert result['temperature']['mean'] == 92.75
assert result['temperature']['median'] == 91.5
assert result['temperature']['std_dev'] == 9.535023160258536
assert result['temperature']['mad'] == 6.0