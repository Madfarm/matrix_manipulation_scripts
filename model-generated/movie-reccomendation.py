import numpy as np

def calculate_cosine_similarity(v1, v2):
    """
    Calculate cosine similarity between two vectors.

    :param v1: The first vector.
    :param v2: The second vector.
    :return: The cosine similarity.
    """
    dot_product = np.dot(v1, v2)
    magnitude_v1 = np.linalg.norm(v1)
    magnitude_v2 = np.linalg.norm(v2)
    cosine_similarity = dot_product / (magnitude_v1 * magnitude_v2)
    return cosine_similarity

def find_k_nearest_neighbors(user_id, ratings, k):
    """
    Find the K-nearest neighbors for a given user.

    :param user_id: The ID of the user.
    :param ratings: The ratings matrix.
    :param k: The number of nearest neighbors to find.
    :return: The IDs of the K-nearest neighbors.
    """
    similarities = []
    for i in range(ratings.shape[0]):
        if i != user_id:
            similarity = calculate_cosine_similarity(ratings[user_id], ratings[i])
            similarities.append((i, similarity))
    similarities.sort(key=lambda x: x[1], reverse=True)
    k_nearest_neighbors = [i[0] for i in similarities[:k]]
    return k_nearest_neighbors

def recommend_movies(user_id, ratings, k):
    """
    Recommend movies for a given user based on the ratings of their K-nearest neighbors.

    :param user_id: The ID of the user.
    :param ratings: The ratings matrix.
    :param k: The number of nearest neighbors to consider.
    :return: A list of movie IDs recommended for the user.
    """
    k_nearest_neighbors = find_k_nearest_neighbors(user_id, ratings, k)
    recommended_movies = set()
    for neighbor in k_nearest_neighbors:
        for movie_id, rating in enumerate(ratings[neighbor]):
            if rating > 0 and ratings[user_id][movie_id] == 0:
                recommended_movies.add(movie_id)
    return list(recommended_movies)

# Create the ratings matrix from the input data
ratings = np.array([
    [4.0, 3.5, 5.0, 0.0, 0.0, 0.0, 0.0],
    [2.5, 1.0, 0.0, 4.0, 0.0, 0.0, 0.0],
    [3.0, 0.0, 4.5, 0.0, 5.0, 0.0, 0.0],
    [0.0, 5.0, 4.0, 0.0, 0.0, 2.0, 0.0],
    [1.5, 0.0, 0.0, 3.5, 0.0, 0.0, 4.0]
])

# Test the program
user_id = 0
k = 2
recommended_movies = recommend_movies(user_id, ratings, k)


# Assertions to validate the calculation
assert np.isclose(calculate_cosine_similarity(ratings[0], ratings[1]), 0.38367410068753877)
assert find_k_nearest_neighbors(user_id, ratings, k) == [3, 2]
assert recommended_movies == [4, 5]