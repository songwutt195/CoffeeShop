from datetime import datetime

class Customer: # Capitalize class names
    def __init__(self, gender: str, age: int):
        self.gender = gender
        self.age = age
        self.type = 'new'

    def discount(self, order, value: int=5): # Apply discount to the order
        if self.type == 'new':
            order.total_price -= value
            self.type = 'active'

class Product:  # Base class for products
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __str__(self):
        return f"This {self.name} is {self.price} baht."
    
class Order:
    def __init__(self, datetime: datetime, customer: Customer):
        self.datetime = datetime
        self.customer = customer
        self.items = []
        self.total_price = 0  # Initialize total_price

    def add_item(self, product: Product):
        self.items.append(product)

class Payment:
    def check_bill(self, order):
        redeemed_points = 0
        for item in order.items:
            if item.type == 'main':
                order.total_price += item.price
            elif item.type == 'free':
                if item.redeem():
                    redeemed_points += 1
        if order.total_price < 0:
            order.total_price = 0
        print(f"This order is {order.total_price} baht and redeemed {redeemed_points} points.")

class Drink(Product): # Inherit from Product
    def __init__(self, name: str, price: int):
        super().__init__(name, price) # Call parent class's __init__
        self.type = 'main'

    def discount(self, value: int):
        discount_amount = min(value, self.price) # Ensure discount doesn't exceed the price
        self.price -= discount_amount

class Snack(Product): # Inherit from Product
    def __init__(self, name: str):
        super().__init__(name, 0) # Call parent class's __init__
        self.type = 'free'

    def redeem(self, quota=1):
        global free_quota
        if free_quota >= quota:
            free_quota -= quota # Reduce dairy free quota
            return True
        else:
            return False

