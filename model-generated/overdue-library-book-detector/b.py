import pandas as pd
from datetime import datetime, timedelta


def detect_overdue_books(df):
    # Convert 'Borrowed Date' column to datetime format
    df['Borrowed Date'] = pd.to_datetime(df['Borrowed Date'])


    # Calculate the difference between today and the borrowed date
    df['Days Since Borrowed'] = (datetime.today() - df['Borrowed Date']).dt.days


    # Filter out books that have been borrowed for more than 30 days
    overdue_books = df[df['Days Since Borrowed'] > 30]


    return overdue_books


# Test the function
data = [
    {'Book ID': 1, 'Book Title': 'The Lord of the Rings', 'Borrower ID': 25, 'Borrower Name': 'John Doe', 'Borrowed Date': '2024-03-15'},
    {'Book ID': 2, 'Book Title': 'Pride and Prejudice', 'Borrower ID': 18, 'Borrower Name': 'Jane Smith', 'Borrowed Date': '2024-03-20'},
    {'Book ID': 1, 'Book Title': 'The Lord of the Rings', 'Borrower ID': 32, 'Borrower Name': None, 'Borrowed Date': '2024-03-22'},
    {'Book ID': 3, 'Book Title': 'To Kill a Mockingbird', 'Borrower ID': 18, 'Borrower Name': 'Jane Smith', 'Borrowed Date': '2024-03-25'},
    {'Book ID': 2, 'Book Title': 'Pride and Prejudice', 'Borrower ID': 25, 'Borrower Name': 'John Doe', 'Borrowed Date': '2024-03-30'}
]


df = pd.DataFrame(data)
overdue_books = detect_overdue_books(df)


assert len(overdue_books) == 0