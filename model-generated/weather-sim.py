import numpy as np
from datetime import datetime


# Sample data
data = {
    "Location": ["New York City", "New York City", "Los Angeles", "Los Angeles", "New York City", "Los Angeles"],
    "Date": ["2024-01-01", "2024-01-05", "2024-01-01", "2024-01-05", "2024-02-01", "2024-02-05"],
    "Temperature": [2.5, 7.0, 18.0, 21.0, 1.0, 22.0],
    "Humidity": [65, 60, 50, 40, 70, 35],
    "Precipitation": [0.1, 0.0, 0.0, 0.0, 0.3, 0.0]
}


# Convert date column to datetime objects
data["Date"] = [datetime.strptime(date, "%Y-%m-%d") for date in data["Date"]]


def calculate_temperature_trend(location, start_date, end_date):
    # Filter data for the specified location and time period
    location_data = [row for row in zip(*data.values()) if row[0] == location and start_date <= row[1] <= end_date]


    # Calculate average temperature trend
    temperatures = [row[2] for row in location_data]
    trend = (temperatures[-1] - temperatures[0]) / len(temperatures)


    return trend


# Test the function
assert calculate_temperature_trend("New York City", datetime(2024, 1, 1), datetime(2024, 1, 31)) == 2.25
assert calculate_temperature_trend("Los Angeles", datetime(2024, 1, 1), datetime(2024, 1, 31)) == 1.5