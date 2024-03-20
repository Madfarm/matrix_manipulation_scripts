def calculate_payout(temperatures):
    total_payout = 0
    for temperature in temperatures:
        if temperature < 3500:
            total_payout += 1000
        elif 3500 <= temperature <= 5000:
            total_payout += 2000
        else:
            total_payout += 3000
    return total_payout

# Example usage:
temperatures = [3000, 4000, 5000, 6000, 7000]
print(calculate_payout(temperatures))  # Output: 15000