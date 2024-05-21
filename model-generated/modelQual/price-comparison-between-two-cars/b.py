def compare_gas_prices(distance, price_of_gallon_of_gas):
    # MPG for Honda Pilot
    honda_pilot_mpg = 22

    # Calculate gas consumption for Honda Pilot
    honda_pilot_gas_consumption = distance / honda_pilot_mpg

    # Calculate total cost for Honda Pilot
    honda_pilot_total_cost = honda_pilot_gas_consumption * price_of_gallon_of_gas

    # MPG for Mazda CX-70
    mazda_cx_70_mpg = 25

    # Calculate gas consumption for Mazda CX-70
    mazda_cx_70_gas_consumption = distance / mazda_cx_70_mpg

    # Calculate total cost for Mazda CX-70
    mazda_cx_70_total_cost = mazda_cx_70_gas_consumption * price_of_gallon_of_gas

    # Create a string message with the results
    message = f"For a distance of {distance} miles and a gas price of ${price_of_gallon_of_gas} per gallon:\n" \
              f"Honda Pilot: ${honda_pilot_total_cost:.2f}\n" \
              f"Mazda CX-70: ${mazda_cx_70_total_cost:.2f}"

    return message

# Test the function
price_of_gallon_of_gas = 3.15
distance = 1000
print(compare_gas_prices(distance, price_of_gallon_of_gas))