from product import Product

class Food(Product):
    def __init__(self, name: str, price: float, grams: float) -> None:
        self.name = name
        self.price = price
        self.grams = grams