class Review:
    def __init__(self, id, rating, flavor, establishment):
        self.id = id
        self.rating = rating
        self.flavor = flavor
        self.establishment = establishment

class ReviewManager:
    def __init__(self):
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def get_review(self, id):
        for review in self.reviews:
            if review.id == id:
                return review
        return None

    def update_review(self, id, rating=None, flavor=None, establishment=None):
        review = self.get_review(id)
        if review:
            if rating:
                review.rating = rating
            if flavor:
                review.flavor = flavor
            if establishment:
                review.establishment = establishment
        else:
            print("Review not found")

    def delete_review(self, id):
        review = self.get_review(id)
        if review:
            self.reviews.remove(review)
        else:
            print("Review not found")

# Testing the program
review_manager = ReviewManager()

review1 = Review(1, 4, "Chocolate", "Baskin-Robbins")
review2 = Review(2, 5, "Strawberry", "Haagen-Dazs")
review3 = Review(3, 3, "Vanilla", "Cold Stone Creamery")

review_manager.add_review(review1)
review_manager.add_review(review2)
review_manager.add_review(review3)

print(review_manager.get_review(1).rating)  # Output: 4
print(review_manager.get_review(2).flavor)  # Output: Strawberry
print(review_manager.get_review(3).establishment)  # Output: Cold Stone Creamery

review_manager.update_review(1, rating=5)
print(review_manager.get_review(1).rating)  # Output: 5

review_manager.delete_review(2)
print(review_manager.get_review(2))  # Output: None