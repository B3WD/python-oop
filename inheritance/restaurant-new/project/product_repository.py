from project.product import Product

class ProductRepository:
    def __init__(self) -> None:
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for p_obj in self.products:
            if p_obj.name == product_name:
                return p_obj

    def remove(self, product_name: str):
        p_obj_to_remove = self.find(product_name)
        if p_obj_to_remove is not None:
            self.products.remove(p_obj_to_remove)

    def __repr__(self) -> str:
        msgs = []
        for p_obj in self.products:
            inner_msg = f"{p_obj.name}: {p_obj.quantity}"
            msgs.append(inner_msg)

        return '\n'.join(msgs) 