import random

def calculate_return(initial_investment, years):
    total = initial_investment
    for _ in range(years):
        gain = random.uniform(0.06, 0.10)
        total *= (1 + gain)
    return total

initial_investment = 200000000000  # 200 billion
years = 5

final_amount = calculate_return(initial_investment, years)
percentage_increase = ((final_amount - initial_investment) / initial_investment) * 100

print(f"Final amount after {years} years: ${final_amount:.2f}")
print(f"Percentage increase from the original: {percentage_increase:.2f}%")