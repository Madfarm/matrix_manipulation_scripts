def calculate_efficiency(brand, price, protein):
    efficiency = protein / price
    return efficiency

# List of cat food brands, their prices, and protein content
brands = [
    {"name": "Purina Friskies", "price": 10.99, "protein": 30},
    {"name": "Whiskas", "price": 12.99, "protein": 25},
    {"name": "Fancy Feast", "price": 14.99, "protein": 35},
    {"name": "Meow Mix", "price": 11.99, "protein": 28},
    {"name": "Royal Canin", "price": 16.99, "protein": 32}
]

# Calculate efficiency for each brand
efficiencies = []
for brand in brands:
    efficiency = calculate_efficiency(brand["name"], brand["price"], brand["protein"])
    efficiencies.append({"brand": brand["name"], "efficiency": efficiency})

# Sort efficiencies in descending order
efficiencies.sort(key=lambda x: x["efficiency"], reverse=True)

# Print the most efficient brand
print("The most efficient cat food brand is:", efficiencies[0]["brand"])