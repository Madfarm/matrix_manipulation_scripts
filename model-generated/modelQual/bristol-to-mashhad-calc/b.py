def predict_temperature(miles):
    # Define the minimum and maximum temperatures
    min_temp = 64.4  # Bristol, UK
    max_temp = 84.2  # Mashhad, Iran

    # Calculate the temperature based on the miles
    temperature = (max_temp - min_temp) * (miles / 4071) + min_temp

    return temperature

# Test the function
miles = 2035
predicted_temperature = predict_temperature(miles)
print(f"The predicted temperature at mile {miles} is {predicted_temperature} degrees Fahrenheit.")