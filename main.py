class Product:
    def __init__(self, name, price, amount):
        self._name = name
        self._price = price
        self._amount = amount

class User:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def return_name(self):
        return self._name

class Order:
    def __init__(self):
        self.user_products = tuple()

    def add_order(self, user, product):
        self.user_products[user] = product

    # def __str__(self):
    #     for key, products in self.user_products.item:
    #         print(key.return_name, ":", [item.name for item in products])