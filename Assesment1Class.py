class Bike:
    def __init__(self, color, price):
        self.color = color
        self.price = price


testOne = Bike("blue", 89.99)
testTwo = Bike("purple", 25.0)


class AppleBasket:
    def __init__(self, apple_color, apple_quantity):
        self.apple_color = apple_color
        self.apple_quantity = apple_quantity

    def increase(self):
        self.apple_quantity += 1

    def __str__(self):
        return (f"A basket of {self.apple_quantity} {self.apple_color} apples.")


testOne = AppleBasket("green", 17)


class BankAccount:
    def __init__(self, name, amt):
            self.name = name
            self.amt = amt

    def __str__(self):
        return(f"Your account, {self.name}, has {self.amt} dollars.")


t1 = BankAccount("Bob", 100)

