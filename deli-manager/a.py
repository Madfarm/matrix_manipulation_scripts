import datetime

class Product:
    def __init__(self, name, brand, price, expiration_date):
        self.name = name
        self.brand = brand
        self.price = price
        self.expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d")

    def display(self):
        print(f"Name: {self.name}, Brand: {self.brand}, Price: {self.price}, Expiration Date: {self.expiration_date.date()}")

class Meat(Product):
    def __init__(self, name, brand, price, expiration_date, slice_thickness):
        super().__init__(name, brand, price, expiration_date)
        self.slice_thickness = slice_thickness

    def display(self):
        print(f"Name: {self.name}, Brand: {self.brand}, Price: {self.price}, Expiration Date: {self.expiration_date.date()}, Slice Thickness: {self.slice_thickness}")

class Cheese(Product):
    def __init__(self, name, brand, price, expiration_date, age):
        super().__init__(name, brand, price, expiration_date)
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Brand: {self.brand}, Price: {self.price}, Expiration Date: {self.expiration_date.date()}, Age: {self.age}")

# Creating a list to hold all products
products = []

# Adding products
products.append(Meat("Beef", "ABC", 10.99, "2022-12-31", "1 inch"))
products.append(Cheese("Cheddar", "XYZ", 8.49, "2022-11-15", "1 year"))
products.append(Product("Lettuce", "PQR", 2.49, "2022-10-01"))

# Displaying all products
for product in products:
    product.display()
    print()

# Deleting a product
del products[1]

# Displaying all products after deletion
for product in products:
    product.display()
    print()