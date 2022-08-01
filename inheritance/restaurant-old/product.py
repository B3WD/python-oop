class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    @property
    def name(self):
        return self.name

    @property
    def price(self):
        return self.price