class Product:
    def __init__(self, name: str, quantity: int) -> None:
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity: int):
        if self.quantity < quantity:
            return

        self.quantity -= quantity

    def increase(self, quantity: int):
        self.quantity += quantity

    def __repr__(self) -> str:
        return f"{self.name}"