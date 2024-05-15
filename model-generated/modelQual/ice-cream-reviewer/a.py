class Review:
    def __init__(self, id, rating, flavor, establishment):
        self.id = id
        self.rating = rating
        self.flavor = flavor
        self.establishment = establishment

class ReviewManager:
    def __init__(self):
        self.reviews = {}

    def add_review(self, id, rating, flavor, establishment):
        if id in self.reviews:
            print("Review with this ID already exists")
            return
        review = Review(id, rating, flavor, establishment)
        self.reviews[id] = review
        print("Review added successfully")

    def get_review(self, id):
        if id not in self.reviews:
            print("Review with this ID does not exist")
            return
        review = self.reviews[id]
        print(f"Rating: {review.rating}")
        print(f"Flavor: {review.flavor}")
        print(f"Establishment: {review.establishment}")

# Test the program
manager = ReviewManager()
manager.add_review(1, 4, "Chocolate", "Baskin-Robbins")
manager.add_review(2, 5, "Vanilla", "Haagen-Dazs")
manager.get_review(1)
manager.get_review(2)