import pandas as pd
import numpy as np


def weighted_average_ratings(df):
    # Check if the input is a pandas DataFrame
    assert isinstance(df, pd.DataFrame), "Input must be a pandas DataFrame"


    # Check if the DataFrame contains the required columns
    required_columns = ['User ID', 'Movie ID', 'Rating']
    assert all(column in df.columns for column in required_columns), "DataFrame must contain 'User ID', 'Movie ID', and 'Rating' columns"


    # Calculate the total number of ratings
    total_ratings = df.shape[0]


    # Calculate the weight for each user
    user_weights = df['User ID'].value_counts() / total_ratings


    # Merge the weights with the original DataFrame
    df = df.merge(user_weights.rename('Weight'), left_on='User ID', right_index=True)


    # Calculate the weighted average rating for each movie
    weighted_ratings = df.groupby('Movie ID').apply(lambda x: np.average(x['Rating'], weights=x['Weight']))


    # Create a new DataFrame with the results
    result_df = pd.DataFrame({'Movie ID': weighted_ratings.index, 'Weighted Average Rating': weighted_ratings.values})


    return result_df


# Example usage
data = {'User ID': [1, 1, 2, 3, 1, 2],
        'Movie ID': [1, 2, 1, 2, 3, 2],
        'Rating': [4, 5, 3, 4, 5, 4]}
df = pd.DataFrame(data)


result_df = weighted_average_ratings(df)
print(result_df)


