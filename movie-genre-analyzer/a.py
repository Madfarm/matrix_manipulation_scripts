class Movie:
    def __init__(self, title, release_date, genre):
        self.title = title
        self.release_date = release_date
        self.genre = genre

movies = [
    Movie("Movie1", 2019, "Action"),
    Movie("Movie2", 2019, "Comedy"),
    Movie("Movie3", 2020, "Drama"),
    Movie("Movie23", 2020, "Action"),
    Movie("Movie4", 2020, "Action"),
    Movie("Movie5", 2021, "Thriller"),
    Movie("Movie6", 2021, "Horror"),
    Movie("Movie7", 2022, "Comedy"),
    Movie("Movie8", 2022, "Romance"),
    Movie("Movie9", 2023, "Action"),
    Movie("Movie10", 2023, "Thriller"),
]

def most_popular_genre_in_year(year):
    genres_in_year = [movie.genre for movie in movies if movie.release_date == year]
    if not genres_in_year:
        return f"No movies released in {year}"
    else:
        return max(set(genres_in_year), key=genres_in_year.count)

def most_popular_year_for_genre(genre):
    years_for_genre = [movie.release_date for movie in movies if movie.genre == genre]
    if not years_for_genre:
        return f"No {genre} movies released"
    else:
        return max(set(years_for_genre), key=years_for_genre.count)

print(most_popular_genre_in_year(2020))  # Output: Action
print(most_popular_year_for_genre("Comedy"))  # Output: 2019