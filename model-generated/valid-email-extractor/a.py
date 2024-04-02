import pandas as pd
import re


# Define the regex pattern
pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'


# Create a pandas Series with the input data
emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])


# Use the str.extract() method to extract the valid emails
valid_emails = emails.str.extract(pattern, expand=False)


# Print the valid emails
print(valid_emails)