def analyze_game_data(game_data):
    analyzed_data = []
    for game in game_data:
        cost_to_produce = game['Cost to Produce (in millions)']
        total_sales = game['Total Sales (in millions)']
        years_to_make = game['Years to Make']
        analyzed_data.append({
            'Game Title': game['Game Title'],
            'Profit': total_sales - cost_to_produce,
            'Profit per Year': (total_sales - cost_to_produce) / years_to_make,
            'Return on Investment': (total_sales / cost_to_produce) * 100
        })
    return analyzed_data

game_data = [
    {'Game Title': 'Galactic Odyssey', 'Cost to Produce (in millions)': 50, 'Total Sales (in millions)': 300, 'Years to Make': 3},
    {'Game Title': 'Mythic Quest', 'Cost to Produce (in millions)': 30, 'Total Sales (in millions)': 200, 'Years to Make': 2},
    {'Game Title': 'Cyberwarriors', 'Cost to Produce (in millions)': 80, 'Total Sales (in millions)': 500, 'Years to Make': 5},
    {'Game Title': 'Dragon\'s Lair', 'Cost to Produce (in millions)': 45, 'Total Sales (in millions)': 250, 'Years to Make': 4}
]

analyzed_data = analyze_game_data(game_data)
print(analyzed_data)