class Book:
    def __init__(self, title, author, genre, publication_year, keywords):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.keywords = keywords

# Hardcoded book database
books = [
    Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960, ["race", "injustice"]),
    Book("1984", "George Orwell", "Dystopian Fiction", 1949, ["surveillance", "future"]),
    Book("Pride and Prejudice", "Jane Austen", "Romance", 1813, ["love", "marriage"]),
    # Add 97 more books...
]

def recommend_books(genres=None, authors=None, publication_years=None, keywords=None, num_books=10):
    # Create a copy of the book list so we don't modify the original
    available_books = books[:]

    if genres:
        available_books = [book for book in available_books if book.genre in genres]
    if authors:
        available_books = [book for book in available_books if book.author in authors]
    if publication_years:
        available_books = [book for book in available_books if book.publication_year in publication_years]
    if keywords:
        available_books = [book for book in available_books if any(keyword in book.keywords for keyword in keywords)]

    # Rank the books based on how well they match the user's preferences
    available_books.sort(key=lambda book: (
        -len([genre for genre in book.genre if genre in genres]),
        -len([author for author in book.author if author in authors]),
        -len([keyword for keyword in book.keywords if keyword in keywords]),
    ), reverse=True)

    return available_books[:num_books]

import threading
import queue

book_queue = queue.Queue()

def handle_book_request(genres=None, authors=None, publication_years=None, keywords=None, num_books=10):
    book_queue.put((genres, authors, publication_years, keywords, num_books))

def book_request_handler():
    while True:
        request = book_queue.get()
        print(recommend_books(*request))
        book_queue.task_done()

threading.Thread(target=book_request_handler, daemon=True).start()

# Now you can make book requests from any thread
threading.Thread(target=handle_book_request, args=(["Fiction"], ["George Orwell"], [1949], ["surveillance"])).start()

print(recommend_books([
    Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960, ["race", "injustice"]),
    Book("1984", "George Orwell", "Dystopian Fiction", 1949, ["surveillance", "future"]),
    Book("Pride and Prejudice", "Jane Austen", "Romance", 1813, ["love", "marriage"]),
    # Add 97 more books...
]))