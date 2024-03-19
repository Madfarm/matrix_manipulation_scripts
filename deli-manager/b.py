from datetime import datetime

class Product:
    def __init__(self, expiration_date, name, brand, price):
        self.expiration_date = expiration_date
        self.name = name
        self.brand = brand
        self.price = price

    def display(self):
        print(f"Name: {self.name}, Brand: {self.brand}, Expiration Date: {self.expiration_date}, Price: {self.price}")

class Meat(Product):
    def __init__(self, expiration_date, name, brand, price, slice_thickness):
        super().__init__(expiration_date, name, brand, price)
        self.slice_thickness = slice_thickness

    def display(self):
        print(f"Name: {self.name}, Brand: {self.brand}, Expiration Date: {self.expiration_date}, Price: {self.price}, Slice Thickness: {self.slice_thickness}")

class Cheese(Product):
    def __init__(self, expiration_date, name, brand, price, age):
        super().__init__(expiration_date, name, brand, price)
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Brand: {self.brand}, Expiration Date: {self.expiration_date}, Price: {self.price}, Age: {self.age}")

class Deli:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def delete_product(self, product):
        self.products.remove(product)

    def display_products(self):
        for product in self.products:
            product.display()

# create deli
deli = Deli()

# create products
ham = Meat(datetime(2024, 4, 1), "Ham", "Smithfield", 5.99, "1/8 inch")
cheddar = Cheese(datetime(2024, 3, 1), "Cheddar", "Muenster", 3.99, "1 year")

# add products to deli
deli.add_product(ham)
deli.add_product(cheddar)

# display products
deli.display_products()

# delete a product
deli.delete_product(ham)

# display products
deli.display_products()