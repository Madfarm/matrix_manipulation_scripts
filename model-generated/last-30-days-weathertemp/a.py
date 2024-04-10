import pandas as pd
from datetime import datetime, timedelta


# Create a list of dates for the last 30 days
dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(30)]


# Create a DataFrame with the dates and two empty columns
df = pd.DataFrame({'dates': dates, 'weather': '', 'temp': ''})


# Print the DataFrame
print(df)