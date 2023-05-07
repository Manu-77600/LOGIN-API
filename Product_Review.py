class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
        self.reviews = []
    
    def add_review(self, review):
        self.reviews.append(review)
    
    def average_rating(self):
        if len(self.reviews) == 0:
            return 0
        total_rating = sum(review.rating for review in self.reviews)
        return total_rating / len(self.reviews)

class Review:
    def __init__(self, username, rating, comment):
        self.username = username
        self.rating = rating
        self.comment = comment

product = Product("Smartphone", 599, "A high-end smartphone with advanced features")

product.add_review(Review("iphone", 5, "Great phone overall"))
product.add_review(Review("oneplus", 4.5, "Awesome phone"))
product.add_review(Review("Nokia", 4, "Decent phone"))

print(f"Average rating: {product.average_rating()}")
for review in product.reviews:
    print(f"{review.username}: {review.rating} stars - {review.comment}")
