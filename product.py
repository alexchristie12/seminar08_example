"""CP104 Week 08 Seminar - Product Class"""


class Product:
    def __init__(self, name="", price=0.00):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}, ${self.price:.2f}"
