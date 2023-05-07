class Product:
    def __init__(self, name, price, description, rating):
        self.name = name
        self.price = price
        self.description = description
        self.rating = rating
    
    def __str__(self):
        return f"{self.name} (${self.price}): {self.description}, {self.rating} stars"

class ProductCatalog:
    def __init__(self, products):
        self.products = products
    
    def get_products_sorted_by_rating(self):
        return sorted(self.products, key=lambda p: p.rating, reverse=True)
    
    def get_products_by_page(self, page_number, page_size):
        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size
        return self.products[start_index:end_index]

# Example usage:
products = [
    Product("Smartphone", 599, "A high-end smartphone with advanced features", 4.5),
    Product("Laptop", 999, "A powerful laptop for gaming and productivity", 4.2),
    Product("Tablet", 299, "A lightweight and portable tablet for entertainment and browsing", 4.0),
    Product("Headphones", 99, "High-quality headphones with noise cancellation", 4.8),
    Product("Smartwatch", 199, "A feature-packed smartwatch with fitness tracking and notifications", 3.9),
]

catalog = ProductCatalog(products)

sorted_products = catalog.get_products_sorted_by_rating()
for product in sorted_products:
    print(product)

page_number = 2
page_size = 2
page_products = catalog.get_products_by_page(page_number, page_size)
for product in page_products:
    print(product)
