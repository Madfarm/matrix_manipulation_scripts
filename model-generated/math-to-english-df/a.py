import pandas as pd
import numpy as np


def generate_scores(df):
    # Check if 'Student Name' column exists in the DataFrame
    assert 'Student Name' in df.columns, "'Student Name' column not found in the DataFrame"


    # Generate Math Score and English Score columns
    df['Math Score'] = np.random.randint(60, 101, size=len(df))
    df['English Score'] = (df['Math Score'] * 1.2) + 5


    # Check if the generated scores are within the expected range
    assert (df['Math Score'] >= 60).all() and (df['Math Score'] <= 100).all(), "Math Score is out of range"
    assert (df['English Score'] >= 77).all() and (df['English Score'] <= 125).all(), "English Score is out of range"


    return df


data = {'Student Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan']}
df = pd.DataFrame(data)
print(generate_scores(df))