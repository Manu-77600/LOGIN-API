import csv

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    
    def __str__(self):
        return f"{self.name} (${self.price}): {self.description}"

class ProductCatalog:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def load_products_from_csv(self, filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = Product(row['name'], float(row['price']), row['description'])
                self.add_product(product)

catalog = ProductCatalog()
catalog.load_products_from_csv('products.csv')

for product in catalog.products:
    print(product)
