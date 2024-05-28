import pandas as pd

# Create a DataFrame
data = {
    "Brand": ["Coca-Cola", "Pepsi", "Mountain Dew", "Dr Pepper"],
    "Parent Company": ["Coca-Cola Co.", "PepsiCo", "PepsiCo", "Keurig Dr Pepper"],
    "Jan": [200, 180, 90, 80],
    "Feb": [190, 170, 85, 75],
    "Mar": [210, 190, 95, 85],
    "Apr": [220, 200, 100, 90],
    "May": [230, 210, 105, 95],
    "Jun": [240, 220, 110, 100],
    "Jul": [250, 230, 115, 105],
    "Aug": [240, 220, 110, 100],
    "Sep": [230, 210, 105, 95],
    "Oct": [220, 200, 100, 90],
    "Nov": [210, 190, 95, 85],
    "Dec": [200, 180, 90, 80]
}
df = pd.DataFrame(data)

# Calculate the median absolute deviation for each brand
df['MAD'] = df.iloc[:, 2:].apply(lambda x: x.abs().median(), axis=1)

# Find the parent company with the highest average median absolute deviation
df['Parent Company MAD'] = df.groupby('Parent Company')['MAD'].transform('mean')
max_mad_parent_company = df.loc[df['Parent Company MAD'].idxmax()]

print("Parent company with the highest average median absolute deviation:", max_mad_parent_company['Parent Company'])