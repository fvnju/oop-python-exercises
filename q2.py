class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, quantity):
        if quantity < 10:
            discount = 0
        elif 10 <= quantity <= 99:
            discount = 0.10
        else:
            discount = 0.20

        total_price = quantity * self.price * (1 - discount)
        return total_price

    def make_purchase(self, quantity):
        if quantity > self.amount:
            raise ValueError(f"Not enough {self.name} in stock.")
        self.amount -= quantity
        return f"Purchase successful. {self.amount} items left."

# Test usage:
product = Product("Widget", 200, 10.00)
print(product.get_price(5))
print(product.get_price(20))
print(product.get_price(150))
print(product.make_purchase(50))
