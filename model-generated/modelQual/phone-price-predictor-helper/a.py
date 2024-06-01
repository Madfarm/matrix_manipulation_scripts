def predict_price(years_prices, year_to_predict):
    # Convert dictionary to list of tuples sorted by year
    sorted_years_prices = sorted(years_prices.items())

    # Calculate the average price increase per year
    total_price_increase = 0
    for i in range(1, len(sorted_years_prices)):
        total_price_increase += sorted_years_prices[i][1] - sorted_years_prices[i-1][1]
    average_price_increase = total_price_increase / (len(sorted_years_prices) - 1)

    # Find the price of the most recent year
    most_recent_year_price = sorted_years_prices[-1][1]

    # Predict the price for the given year
    predicted_price = most_recent_year_price + (average_price_increase * (year_to_predict - sorted_years_prices[-1][0]))

    return predicted_price

# Test the function
years_prices = {2020: 1000, 2021: 1100, 2022: 1200, 2023: 1300}
year_to_predict = 2024
print(predict_price(years_prices, year_to_predict))