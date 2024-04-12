import pandas as pd
from datetime import date, timedelta


def detect_overdue_books(df):
    # Get today's date
    today = date.today()


    # Calculate the overdue date (30 days ago)
    overdue_date = today - timedelta(days=30)


    # Convert 'Borrowed Date' column to datetime format
    df['Borrowed Date'] = pd.to_datetime(df['Borrowed Date'])


    # Filter books that are overdue
    overdue_books = df[df['Borrowed Date'] < overdue_date]


    return overdue_books


# Create a DataFrame from given data
data = [
        {'Book ID': 1, 'Book Title': 'The Lord of the Rings', 'Borrower ID': 25, 'Borrower Name': 'John Doe', 'Borrowed Date': '2024-03-15'},
        {'Book ID': 2, 'Book Title': 'Pride and Prejudice', 'Borrower ID': 18, 'Borrower Name': 'Jane Smith', 'Borrowed Date': '2024-03-20'},
        {'Book ID': 3, 'Book Title': 'To Kill a Mockingbird', 'Borrower ID': 18, 'Borrower Name': 'Jane Smith', 'Borrowed Date': '2024-03-25'},
        {'Book ID': 2, 'Book Title': 'Pride and Prejudice', 'Borrower ID': 25, 'Borrower Name': 'John Doe', 'Borrowed Date': '2024-04-01'},
]
df = pd.DataFrame(data)


overdue_books = detect_overdue_books(df)
print(overdue_books)