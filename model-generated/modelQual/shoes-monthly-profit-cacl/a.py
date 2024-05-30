import pandas as pd

# Data for New Balance x Miu Miu 530 SL
new_balance_data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Units Sold': [40, 35, 45, 50, 55, 40, 50, 45, 55, 45, 40, 50],
    'Sale Price (USD)': [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250],
    'Production Cost (USD)': [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
}

# Data for Nike x Bode Astro Grabber
nike_data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Units Sold': [60, 55, 65, 70, 75, 60, 70, 65, 75, 65, 60, 70],
    'Sale Price (USD)': [220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220],
    'Production Cost (USD)': [90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
}

# Data for CLOT x adidas Superstar
clot_data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Units Sold': [50, 45, 55, 60, 65, 50, 60, 55, 65, 55, 50, 65],
    'Sale Price (USD)': [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    'Production Cost (USD)': [80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80]
}

# Create dataframes
new_balance_df = pd.DataFrame(new_balance_data)
nike_df = pd.DataFrame(nike_data)
clot_df = pd.DataFrame(clot_data)

# Calculate profit for each month
new_balance_df['Profit'] = new_balance_df['Units Sold'] * (new_balance_df['Sale Price (USD)'] - new_balance_df['Production Cost (USD)'])
nike_df['Profit'] = nike_df['Units Sold'] * (nike_df['Sale Price (USD)'] - nike_df['Production Cost (USD)'])
clot_df['Profit'] = clot_df['Units Sold'] * (clot_df['Sale Price (USD)'] - clot_df['Production Cost (USD)'])

# Calculate mean profit for each shoe
new_balance_mean_profit = new_balance_df['Profit'].mean()
nike_mean_profit = nike_df['Profit'].mean()
clot_mean_profit = clot_df['Profit'].mean()

# Determine the shoe with the highest mean profit
shoes = {'New Balance x Miu Miu 530 SL': new_balance_mean_profit, 'Nike x Bode Astro Grabber': nike_mean_profit, 'CLOT x adidas Superstar': clot_mean_profit}
max_profit_shoe = max(shoes, key=shoes.get)

# Print the result
print(f"The shoe with the highest mean profit is {max_profit_shoe}.")