import pandas as pd
from datetime import datetime, timedelta


# Get today's date
today = datetime.today()


# Create a list of the last 30 days
dates = [today - timedelta(days=i) for i in range(30)]


# Create a DataFrame with the dates
df = pd.DataFrame(dates, columns=['dates'])


# Add two empty columns
df['weather'] = ''
df['temp'] = ''


# Print the DataFrame
print(df)