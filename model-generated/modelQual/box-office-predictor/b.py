import pandas as pd
from sklearn.linear_model import LinearRegression

# List of movies, their genre, and box office amount
movies = [
    {'title': 'Dune: Part Two', 'genre': 'Science Fiction', 'box_office': 82500000},
    {'title': 'Movie1', 'genre': 'Action', 'box_office': 10000000},
    {'title': 'Movie2', 'genre': 'Comedy', 'box_office': 20000000},
    {'title': 'Movie3', 'genre': 'Science Fiction', 'box_office': 30000000},
    {'title': 'Movie4', 'genre': 'Romance', 'box_office': 40000000},
]

# Movie to predict
movie_to_predict = {'title': 'Movie5', 'genre': 'Science Fiction'}

# Create a DataFrame from the list of movies
df = pd.DataFrame(movies)

# Create a Linear Regression model
model = LinearRegression()

# Filter the DataFrame to include only movies with the same genre as the movie to predict
df_genre = df[df['genre'] == movie_to_predict['genre']]

# Train the model on the filtered DataFrame
model.fit(df_genre[['box_office']], df_genre[['box_office']])

# Predict the box office amount for the movie to predict
prediction = model.predict([[0]])[0][0]

print(f'The predicted box office amount for {movie_to_predict["title"]} is {prediction:.2f}')