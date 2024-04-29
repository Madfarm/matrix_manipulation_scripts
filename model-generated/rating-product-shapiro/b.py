import numpy as np
from scipy import stats


def analyze_product_ratings(product_ratings):
    # Calculate the overall average rating of the products
    average_rating = np.mean(product_ratings)
    assert np.isclose(average_rating, 3.85), f"Expected average rating to be approximately 3.85, but got {average_rating}"


    # Determine the percentage of ratings that are 4 or 5
    positive_reviews = [rating for rating in product_ratings if rating >= 4]
    percentage_positive = (len(positive_reviews) / len(product_ratings)) * 100
    assert np.isclose(percentage_positive, 60.0), f"Expected percentage of positive reviews to be approximately 60.0%, but got {percentage_positive}%"


    # Compute the standard deviation of the ratings
    std_dev = np.std(product_ratings)
    assert np.isclose(std_dev, 1.077, atol=0.001), f"Expected standard deviation to be approximately 1.077, but got {std_dev}"


    # Identify the most common rating given by the users
    most_common_rating = stats.mode(product_ratings)[0][0]
    assert most_common_rating == 4, f"Expected most common rating to be 4, but got {most_common_rating}"


    # Test whether the ratings follow a normal distribution using a Shapiro-Wilk test
    w_stat, p_value = stats.shapiro(product_ratings)
    assert p_value < 0.05, f"Expected p-value to be less than 0.05, but got {p_value}"


# Test the function
product_ratings = [4, 5, 3, 4, 2, 5, 4, 3, 4, 5, 3, 4, 5, 2, 3, 4, 5, 4, 3, 3]
analyze_product_ratings(product_ratings)