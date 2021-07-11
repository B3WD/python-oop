from Point import Point

class Rectangle:

    def __init__(self, p, w, h):
        self.CornerPoint = p
        self.width = w
        self.height = h

    def __str__(self):
        return f"Rectangle {self.width} by {self.height}, at {self.CornerPoint}."

    def area(self):

        return self.width * self.height


r1 = Rectangle(Point(3, 4), 5, 6)
print(r1)