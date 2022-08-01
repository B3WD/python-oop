from project.beverage.hot_beverage import HotBeverage

class Coffee(HotBeverage):
    COFFEE_MILLILITERS = 50 
    COFFEE_PRICE = 3.50

    def __init__(self, name: str, price: float, milliliters: float, caffeine: float) -> None:
        self.name = name
        self.price = Coffee.COFFEE_PRICE
        self.milliliters = Coffee.COFFEE_MILLILITERS
        self.caffeine = caffeine

    @property
    def caffeine(self):
        return self.caffeine