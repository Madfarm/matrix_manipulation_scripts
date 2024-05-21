def compare_gas_prices(price_of_gallon_of_gas, distance):
    # Assume the Honda Pilot's average mpg is 22.5
    honda_pilot_mpg = 22.5
    mazda_cx70_mpg = 25

    # Calculate the gas consumption for each vehicle
    honda_pilot_gas_consumption = distance / honda_pilot_mpg
    mazda_cx70_gas_consumption = distance / mazda_cx70_mpg

    # Calculate the total price of gas for each vehicle
    honda_pilot_total_price = honda_pilot_gas_consumption * price_of_gallon_of_gas
    mazda_cx70_total_price = mazda_cx70_gas_consumption * price_of_gallon_of_gas

    # Return the total price from both cars stored in a string message
    return f"The total price of gas for the Honda Pilot is ${honda_pilot_total_price:.2f} and for the Mazda CX-70 is ${mazda_cx70_total_price:.2f}."

# Test the function with the given input
price_of_gallon_of_gas = 3.15
distance = 1000
print(compare_gas_prices(price_of_gallon_of_gas, distance))