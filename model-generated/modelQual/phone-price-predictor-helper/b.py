def predict_price(price_dict, year_to_predict):
    # Calculate the average price increase per year
    total_increase = 0
    for i in range(1, len(price_dict)):
        total_increase += price_dict[i] - price_dict[i-1]
    avg_increase = total_increase / (len(price_dict) - 1)

    # Predict the price for the given year
    predicted_price = price_dict[len(price_dict)-1] + avg_increase * (year_to_predict - len(price_dict))

    return predicted_price

# Test the function
price_dict = {2020: 1000, 2021: 1100, 2022: 1200, 2023: 1300}
year_to_predict = 2024
print(predict_price(price_dict, year_to_predict))