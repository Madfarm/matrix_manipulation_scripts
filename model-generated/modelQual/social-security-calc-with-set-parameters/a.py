import math

def calculate_social_security_cost(population, growth_rate, mortality_rate, social_security_per_person, year):
    # Calculate the number of people who will be alive in the specified year
    alive_population = population * math.pow(1 + growth_rate, year - 2024)
    
    # Calculate the number of people who will die in the specified year
    deaths = alive_population * (1 - mortality_rate)
    
    # Calculate the total social security cost for the specified year
    total_cost = deaths * social_security_per_person
    
    return total_cost

# Test the function
population = 342000000  # Initial Social Security area population in 2024
growth_rate = 0.015  # Annual population growth rate
mortality_rate = 0.075  # Annual mortality rate
social_security_per_person = 10500  # Social Security per person per year
year = 2043  # Specified year

total_cost = calculate_social_security_cost(population, growth_rate, mortality_rate, social_security_per_person, year)
print(f"The total social security cost in {year} is: ${total_cost:,.2f}")