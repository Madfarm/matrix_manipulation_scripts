import numpy as np


# Sample user ratings data
user_ratings = np.array([
    [4.5, 3.0, 5.0, 2.0, 1.0],
    [3.5, 4.0, 2.5, 4.5, 1.5],
    [5.0, 2.0, 4.0, 1.0, 3.5],
    [2.0, 4.5, 1.5, 3.0, 5.0],
    [1.0, 3.0, 4.5, 2.5, 5.0]
])


# Sample song features data
song_features = np.array([
    [1, 0, 0, 0, 0],  # Rock
    [0, 1, 0, 0, 0],  # Pop
    [0, 0, 1, 0, 0],  # Electronic
    [0, 0, 0, 1, 0],  # Country
    [0, 0, 0, 0, 1]  # Hip Hop
])


def calculate_cosine_similarity(user1_ratings, user2_ratings):
    """
    Calculate the cosine similarity between two user rating vectors.


    Args:
        user1_ratings (np.array): Ratings of user 1.
        user2_ratings (np.array): Ratings of user 2.


    Returns:
        float: Cosine similarity between the two users' rating patterns.
    """
    assert len(user1_ratings) == len(user2_ratings), "User rating arrays must have the same length."


    dot_product = np.dot(user1_ratings, user2_ratings)
    magnitude_user1 = np.linalg.norm(user1_ratings)
    magnitude_user2 = np.linalg.norm(user2_ratings)


    cosine_similarity = dot_product / (magnitude_user1 * magnitude_user2)
    return cosine_similarity


def encode_song_info(song_id, genre, artist):
    """
    Encode song information into a NumPy array.


    Args:
        song_id (str): ID of the song.
        genre (str): Genre of the song.
        artist (str): Artist of the song.


    Returns:
        np.array: Encoded song information.
    """
    genres = ['Rock', 'Pop', 'Electronic', 'Country', 'Hip Hop']
    artists = ['Band X', 'Singer Y', 'DJ Z', 'Artist A', 'Group B']


    genre_index = genres.index(genre)
    artist_index = artists.index(artist)


    encoded_song_info = np.zeros(len(genres) + len(artists))
    encoded_song_info[genre_index] = 1
    encoded_song_info[len(genres) + artist_index] = 1


    return encoded_song_info


# Test the functions
user1_ratings = user_ratings[0]
user2_ratings = user_ratings[1]


cosine_similarity = calculate_cosine_similarity(user1_ratings, user2_ratings)
print("Cosine Similarity:", cosine_similarity)


song_id = "song_1"
genre = "Rock"
artist = "Band X"


encoded_song_info = encode_song_info(song_id, genre, artist)
print("Encoded Song Info:", encoded_song_info)