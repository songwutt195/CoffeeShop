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
        # self.total_price += product.price

class Payment:
    def check_bill(self, order, free_quota):
        redeemed_points = 0
        for item in order.items:
            if item.type == 'main':
                order.total_price += item.price
            elif item.type == 'free':
                if item.redeem(free_quota):
                    redeemed_points += 1
        if order.total_price < 0:
            order.total_price = 0
        return f"This order is {order.total_price} baht and redeemed {redeemed_points} points.", free_quota-redeemed_points

class Drink(Product): # Inherit from Product
    def __init__(self, name: str, price: int):
        super().__init__(name, price) # Call parent class's __init__
        self.type = 'main'

    def discount(self, value: int):
        discount_amount = min(value, self.price) # Ensure discount doesn't exceed the price
        self.price -= discount_amount
    
    def copy(self):
        new_self = Drink(self.name, self.price)
        return new_self

class Snack(Product): # Inherit from Product
    def __init__(self, name: str):
        super().__init__(name, 0) # Call parent class's __init__
        self.type = 'free'

    def redeem(self, free_quota, quota=1):
        if free_quota >= quota:
            free_quota -= quota # Reduce dairy free quota
            return True
        else:
            return False
    
    def copy(self):
        new_self = Snack(self.name)
        return new_self

class MemberCustomer(Customer):
    def __init__(self, id: int, name: str, gender: str, age: int):
        super().__init__(gender, age)
        self.id = id
        self.name = name
        self.tpe = 'member'
        self.points = 100  # Initial points for members

    def discount(self, order):
        if self.points > 10: # 10% discount for members
            for item in order.items:
                if item.type == 'main':
                    discount_amount = 0.1 * item.price
                    item.discount(int(discount_amount))
            self.points -= 10