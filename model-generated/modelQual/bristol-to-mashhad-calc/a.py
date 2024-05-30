def predict_temperature(mile):
    # Define the temperatures for Bristol and Mashhad
    bristol_temp = 64.4
    mashhad_temp = 84.2  # Convert 29 degrees Celsius to Fahrenheit

    # Calculate the temperature for the given mile
    temperature = bristol_temp + ((mashhad_temp - bristol_temp) / 4071) * mile

    return temperature

# Test the function
print(predict_temperature(2035))