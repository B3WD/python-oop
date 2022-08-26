class Shape:
    def __init__(self) -> None:
        raise NotImplementedError

class Square(Shape):
    def __init__(self, x) -> None:
        self.x = x

    
s = Shape()