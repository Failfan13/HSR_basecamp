class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self):
        total = 0
        if self.amount in range(10, 100):
            total = (self.amount*self.price)/100*90
        elif self.amount > 100:
            total = (self.amount*self.price)/100*80
        else:
            total = (self.amount*self.price)
        return total

    def make_purchase(self):
        ...


if __name__ == "__main__":
    prod = Product('milk', 12)
    print(prod.get_price())