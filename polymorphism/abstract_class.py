from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

class Square(Shape):
    def __init__(self, x) -> None:
        self.x = x


s = Shape()