class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Order:
    def __init__(self):
        self.user_products = tuple()

    def add_order(self, user, product):
        self.user_products[user] = product

    def get_total_price(self, user):
        total_price = 0
        for product in self.user_products[user]:
            total_price += product.price
        return total_price