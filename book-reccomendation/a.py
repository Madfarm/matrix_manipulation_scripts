class Book:
    def __init__(self, title, author, genre, publication_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year

    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Publication Year: {self.publication_year}"


class BookRecommendationSystem:
    def __init__(self):
        self.books = [
            Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960),
            Book("1984", "George Orwell", "Dystopian", 1949),
            Book("Pride and Prejudice", "Jane Austen", "Romance", 1813),
            Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925),
            # Add more books here...
        ]

    def recommend_books(self, genre=None, author=None, publication_year=None, title=None, limit=10):
        recommended_books = []
        for book in self.books:
            if (genre is None or book.genre.lower() == genre.lower()) and \
               (author is None or book.author.lower() == author.lower()) and \
               (publication_year is None or book.publication_year == publication_year) and \
               (title is None or title.lower() in book.title.lower()):
                recommended_books.append(book)
        recommended_books.sort(key=lambda book: (book.genre, book.author, book.publication_year, book.title))
        return recommended_books[:limit]

    def handle_requests(self, requests):
        for request in requests:
            genre = request.get('genre')
            author = request.get('author')
            publication_year = request.get('publication_year')
            title = request.get('title')
            limit = request.get('limit', 10)
            recommended_books = self.recommend_books(genre, author, publication_year, title, limit)
            print("Recommended Books:")
            for book in recommended_books:
                print(book)
            print()


def main():
    book_recommendation_system = BookRecommendationSystem()
    requests = [
        {'genre': 'Fiction'},
        {'author': 'George Orwell'},
        {'publication_year': 1960},
        {'title': 'Pride'},
        # Add more requests here...
    ]
    book_recommendation_system.handle_requests(requests)


if __name__ == "__main__":
    main()