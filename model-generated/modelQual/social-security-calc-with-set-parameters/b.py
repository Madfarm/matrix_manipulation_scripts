def calculate_social_security_cost(initial_population, growth_rate, mortality_rate, social_security_per_person, year):
    population = initial_population
    for _ in range(year - 2024):
        population *= (1 + growth_rate / 100)
        population *= (1 - mortality_rate / 100)
    return population * social_security_per_person

# Execute the tool
initial_population = 342000000
growth_rate = 1.5
mortality_rate = 7.5
social_security_per_person = 10500
year = 2043

cost = calculate_social_security_cost(initial_population, growth_rate, mortality_rate, social_security_per_person, year)
print(f"The total cost of social security in the USA in {year} would be approximately ${cost:.2f}")