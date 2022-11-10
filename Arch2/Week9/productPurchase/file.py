class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, amount):
        total = 0
        if amount in range(10, 99):
            total = (amount * self.price) / 100 * 90
        elif amount > 99:
            total = (amount * self.price) / 100 * 80
        else:
            total = (amount * self.price)
        print(round(total))

    def make_purchase(self, amount):
        self.amount -= amount