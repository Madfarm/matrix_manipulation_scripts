import pandas as pd
import numpy as np


def generate_scores(df):
    # Ensure the input is a pandas DataFrame
    assert isinstance(df, pd.DataFrame), "Input must be a pandas DataFrame"


    # Ensure the 'Student Name' column exists in the DataFrame
    assert 'Student Name' in df.columns, "DataFrame must contain 'Student Name' column"


    # Generate random Math Scores
    df['Math Score'] = np.random.randint(60, 101, size=len(df))


    # Calculate English Scores based on Math Scores
    df['English Score'] = (df['Math Score'] * 1.2) + 5


    # Ensure the Math Scores are within the correct range
    assert (df['Math Score'] >= 60).all() and (df['Math Score'] <= 100).all(), "Math Scores must be between 60 and 100"


    return df


data = {'Student Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan']}
df = pd.DataFrame(data)


df = generate_scores(df)
print(df)