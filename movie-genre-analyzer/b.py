class Movie:
    def __init__(self, title, release_date, genre):
        self.title = title
        self.release_date = release_date
        self.genre = genre

movies = [
    Movie("The Shawshank Redemption", 1994, "Drama"),
    Movie("The Godfather", 1972, "Crime"),
    Movie("The Dark Knight", 2008, "Action"),
    Movie("12 Angry Men", 1957, "Drama"),
    Movie("Schindler's List", 1993, "Drama"),
    Movie("The Lord of the Rings: The Return of the King", 2003, "Fantasy"),
    Movie("Pulp Fiction", 1994, "Crime"),
    Movie("Fight Club", 1999, "Drama"),
    Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Fantasy"),
    Movie("Forrest Gump", 1994, "Drama"),
    Movie("Inception", 2010, "Sci-Fi"),
    Movie("The Matrix", 1999, "Sci-Fi"),
    Movie("Goodfellas", 1990, "Crime"),
    Movie("Seven Samurai", 1954, "Action"),
    Movie("Star Wars", 1977, "Sci-Fi"),
    Movie("City of God", 2002, "Drama"),
    Movie("Se7en", 1995, "Thriller"),
    Movie("The Silence of the Lambs", 1991, "Thriller"),
    Movie("It's a Wonderful Life", 1946, "Drama"),
    Movie("Life Is Beautiful", 1997, "Drama"),
    Movie("The Usual Suspects", 1995, "Thriller"),
    Movie("Léon: The Professional", 1994, "Action"),
    Movie("Spirited Away", 2001, "Fantasy"),
    Movie("Saving Private Ryan", 1998, "War"),
    Movie("E.T. the Extra-Terrestrial", 1982, "Sci-Fi"),
    Movie("The Lord of the Rings: The Two Towers", 2002, "Fantasy"),
    Movie("Casablanca", 1942, "Drama"),
    Movie("City Lights", 1931, "Comedy"),
    Movie("Psycho", 1960, "Thriller"),
    Movie("Rear Window", 1954, "Thriller"),
    Movie("Raiders of the Lost Ark", 1981, "Action"),
    Movie("The Princess Bride", 1987, "Fantasy"),
    Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Fantasy"),
    Movie("Star Wars: Episode V - The Empire Strikes Back", 1980, "Sci-Fi"),
    Movie("The Good, the Bad and the Ugly", 1966, "Western"),
    Movie("12 Angry Men", 1957, "Drama"),
    Movie("Schindler's List", 1993, "Drama"),
    Movie("The Dark Knight", 2008, "Action"),
    Movie("Pulp Fiction", 1994, "Crime"),
    Movie("Fight Club", 1999, "Drama"),
    Movie("The Lord of the Rings: The Return of the King", 2003, "Fantasy"),
    Movie("Inception", 2010, "Sci-Fi"),
    Movie("The Matrix", 1999, "Sci-Fi"),
    Movie("Goodfellas", 1990, "Crime"),
    Movie("Seven Samurai", 1954, "Action"),
    Movie("Star Wars", 1977, "Sci-Fi"),
    Movie("City of God", 2002, "Drama"),
    Movie("Se7en", 1995, "Thriller"),
    Movie("The Silence of the Lambs", 1991, "Thriller"),
    Movie("It's a Wonderful Life", 1946, "Drama"),
    Movie("Life Is Beautiful", 1997, "Drama"),
    Movie("The Usual Suspects", 1995, "Thriller"),
    Movie("Léon: The Professional", 1994, "Action"),
    Movie("Spirited Away", 2001, "Fantasy"),
    Movie("Saving Private Ryan", 1998, "War"),
    Movie("E.T. the Extra-Terrestrial", 1982, "Sci-Fi"),
    Movie("The Lord of the Rings: The Two Towers", 2002, "Fantasy"),
    Movie("Casablanca", 1942, "Drama"),
    Movie("City Lights", 1931, "Comedy"),
    Movie("Psycho", 1960, "Thriller"),
    Movie("Rear Window", 1954, "Thriller"),
    Movie("Raiders of the Lost Ark", 1981, "Action"),
    Movie("The Princess Bride", 1987, "Fantasy"),
    Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Fantasy"),
    Movie("Star Wars: Episode V - The Empire Strikes Back", 1980, "Sci-Fi"),
    Movie("The Good, the Bad and the Ugly", 1966, "Western"),
]

def most_popular_genre_in_year(year):
    genres = {}
    for movie in movies:
        if movie.release_date == year:
            if movie.genre in genres:
                genres[movie.genre] += 1
            else:
                genres[movie.genre] = 1
    if genres:
        return max(genres, key=genres.get)
    else:
        return "No movies released in that year"

def most_popular_year_for_genre(genre):
    years = {}
    for movie in movies:
        if movie.genre == genre:
            if movie.release_date in years:
                years[movie.release_date] += 1
            else:
                years[movie.release_date] = 1
    if years:
        return max(years, key=years.get)
    else:
        return "No movies of that genre"

print(most_popular_genre_in_year(1994))
print(most_popular_year_for_genre("Drama"))