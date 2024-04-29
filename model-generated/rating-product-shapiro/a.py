import numpy as np
from scipy import stats


def analyze_ratings(product_ratings):
    # Calculate the overall average rating of the products
    average_rating = np.mean(product_ratings)
    assert round(average_rating, 2) == 3.75, "Incorrect average rating"

    # Determine the percentage of ratings that are 4 or 5
    positive_reviews = len([rating for rating in product_ratings if rating >= 4])
    percentage_positive = (positive_reviews / len(product_ratings)) * 100
    assert round(percentage_positive) == 60, "Incorrect percentage of positive reviews"

    # Compute the standard deviation of the ratings
    std_dev = np.std(product_ratings)
    assert round(std_dev, 2) == 0.94, "Incorrect standard deviation"

    # Identify the most common rating given by the users
    most_common_rating = stats.mode(product_ratings)[0][0]
    assert most_common_rating == 4, "Incorrect most common rating"

    # Test whether the ratings follow a normal distribution using a Shapiro-Wilk test
    w_stat, p_value = stats.shapiro(product_ratings)
    assert round(w_stat, 2) == 0.88, "Incorrect W-statistic"
    assert round(p_value, 4) == 0.0193, "Incorrect p-value"


# Test the function with the given input
product_ratings = [4, 5, 3, 4, 2, 5, 4, 3, 4, 5, 3, 4, 5, 2, 3, 4, 5, 4, 3, 3]
analyze_ratings(product_ratings)