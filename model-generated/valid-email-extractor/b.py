import pandas as pd
import re


# Define the regex pattern
pattern = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'


# Create a pandas Series with emails
emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])


# Define a function to extract valid emails
def extract_emails(text):
    return re.findall(pattern, text)


# Apply the function to the emails Series
valid_emails = emails.apply(extract_emails)


# Print the valid emails
print(valid_emails)