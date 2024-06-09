def calculate_price_per_mg(drinks):
    for drink in drinks:
        price_per_mg = drink['price'] / drink['caffeine_content']
        drink['price_per_mg'] = price_per_mg
    return sorted(drinks, key=lambda x: x['price_per_mg'])


drinks = [
    {'name': 'Thunderbolt Energy', 'price': 2.99, 'caffeine_content': 160},
    {'name': 'Power Surge', 'price': 3.49, 'caffeine_content': 180},
    {'name': 'Lightning Blast', 'price': 2.79, 'caffeine_content': 150},
    {'name': 'Turbo Charge', 'price': 3.99, 'caffeine_content': 200},
    {'name': 'Rocket Fuel', 'price': 4.49, 'caffeine_content': 220},
    {'name': 'Monster Ruby Red', 'price': 2.99, 'caffeine_content': 150},
    {'name': 'Celsius Astro Vibe', 'price': 3.99, 'caffeine_content': 200}
]

drinks = calculate_price_per_mg(drinks)


for drink in drinks:
    print(f"{drink['name']}: ${drink['price_per_mg']:.5f} per mg")