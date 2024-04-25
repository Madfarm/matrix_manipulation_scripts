import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def simulate_stock_price(starting_price, num_days, volatility):
    # Validate input
    assert isinstance(starting_price, (int, float)) and starting_price > 0, "Starting price must be a positive number."
    assert isinstance(num_days, int) and num_days > 0, "Number of days must be a positive integer."
    assert isinstance(volatility, (int, float)) and 0 <= volatility < 1, "Volatility must be between 0 and 1."


    # Create date range
    start_date = datetime.now()
    dates = [start_date + timedelta(days=i) for i in range(num_days)]


    # Generate random price changes
    np.random.seed(42)
    price_changes = np.random.uniform(-volatility, volatility, size=num_days)


    # Calculate daily prices
    prices = [starting_price]
    for change in price_changes:
        prices.append(prices[-1] + prices[-1] * change)


    # Create DataFrame
    df = pd.DataFrame({'Date': dates, 'Price': prices[:-1]})


    # Validate output
    assert len(df) == num_days, "DataFrame length does not match the number of days."
    assert all(df['Price'] > 0), "Prices cannot be negative."


    return df


# Demonstrate the function
df = simulate_stock_price(starting_price=100, num_days=30, volatility=0.05)
print(df)