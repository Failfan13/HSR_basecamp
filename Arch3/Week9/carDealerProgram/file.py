class Car:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold = False
        self.sold_to = None

    def sell(self, customer):
        self.sold = True
        self.sold_to = customer

    def print(self):
        if self.sold is True:
            print(f"{self.brand, self.model, self.color, self.price, self.sold_to.name}")
        else:
            print(f"{self.brand, self.model, self.color, self.price}")


class Customer:
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)


class Motorcycle:
    ...


if __name__ == "__main__":
    ...