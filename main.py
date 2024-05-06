class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def apply_discount(self, percent):
        self.price *= (1 - percent / 100)


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Order:
    def __init__(self):
        self.user_products = {}
        self.status = "New"

    def add_order(self, user, product):
        if user not in self.user_products:
            self.user_products[user] = []
        self.user_products[user].append(product)

    def get_total_price(self, user):
        total_price = 0
        if user in self.user_products:
            for product in self.user_products[user]:
                total_price += product.price
        return total_price
    
    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status


class Inventory:
    def __init__(self):
        self.products = []

    def search_by_name(self, name):
        return [product for product in self.products if name in product.name]

    def filter_by_price(self, min_price, max_price):
        return [product for product in self.products if min_price <= product.price <= max_price]


class Analytics:
    def __init__(self, orders):
        self.orders = orders

    def generate_sales_report(self):
        report = {}
        for order in self.orders:
            for product in order.user_products.values():
                if product.name in report:
                    report[product.name] += 1
                else:
                    report[product.name] = 1
        return report
    
    class Analytics:
        def __init__(self, orders):
            self.orders = orders

        def generate_sales_report(self):
            product_sales = {}
            total_sales = 0
            for order in self.orders:
                for product in order.user_products.values():
                    for item in product:
                        if item.name in product_sales:
                            product_sales[item.name] += 1
                        else:
                            product_sales[item.name] = 1
                        total_sales += item.price

            return {'total_sales': total_sales, 'product_sales': product_sales}

        def generate_product_popularity_report(self):
            popularity = {}
            for order in self.orders:
                for product in order.user_products.values():
                    for item in product:
                        if item.name in popularity:
                            popularity[item.name] += 1
                        else:
                            popularity[item.name] = 1

            # סדר את המוצרים לפי פופולריות
            sorted_popularity = sorted(popularity.items(), key=lambda x: x[1], reverse=True)
            return sorted_popularity


# יצירת מוצרים
product1 = Product("Laptop", 1200, 10)
product2 = Product("Mouse", 25, 100)
product3 = Product("Keyboard", 75, 50)

# יצירת משתמש
user1 = User("Alice", "alice@example.com")

# יצירת הזמנה והוספת מוצרים להזמנה
order1 = Order()
order1.add_order(user1, product1)
order1.add_order(user1, product2)

# יצירת דוחות
orders_list = [order1]  # רשימה של ההזמנות
analytics = Analytics(orders_list)

# גנרציה של דוח מכירות
sales_report = analytics.generate_sales_report()
product_popularity = analytics.generate_product_popularity_report()

print(sales_report)
print(product_popularity)
