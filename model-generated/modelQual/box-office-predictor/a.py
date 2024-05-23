def predict_box_office(movie_list, movie_to_predict):
    # Create a dictionary to store the genres and their average box office amounts
    genre_box_office = {}
    
    # Iterate over the movies in the list
    for movie in movie_list:
        # If the genre is not in the dictionary, add it with the box office amount
        if movie['genre'] not in genre_box_office:
            genre_box_office[movie['genre']] = [movie['box_office']]
        # If the genre is already in the dictionary, append the box office amount
        else:
            genre_box_office[movie['genre']].append(movie['box_office'])
    
    # Calculate the average box office amount for each genre
    for genre in genre_box_office:
        genre_box_office[genre] = sum(genre_box_office[genre]) / len(genre_box_office[genre])
    
    # Predict the box office amount for the movie to predict
    predicted_box_office = genre_box_office[movie_to_predict['genre']]
    
    return predicted_box_office

# Test the function
movie_list = [
    {'name': 'Movie 1', 'genre': 'Action', 'box_office': 10000000},
    {'name': 'Movie 2', 'genre': 'Comedy', 'box_office': 5000000},
    {'name': 'Movie 3', 'genre': 'Action', 'box_office': 12000000},
    {'name': 'Movie 4', 'genre': 'Drama', 'box_office': 8000000},
    {'name': 'Movie 5', 'genre': 'Comedy', 'box_office': 6000000},
]

movie_to_predict = {'name': 'Movie 6', 'genre': 'Action'}

predicted_box_office = predict_box_office(movie_list, movie_to_predict)

print(f'The predicted box office amount for {movie_to_predict["name"]} is ${predicted_box_office:.2f}')