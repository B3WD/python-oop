from product import Product

class Beverage(Product):
    def __init__(self, name: str, price: float, milliliters: float) -> None:
        super().__init__(name, price)
        self.milliliters = milliliters

    @property
    def milliliters(self):
        return self.milliliters