class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __getDxDy(self, target):
        dx = self.x - target.x
        dy = self.y - target.y
        return dx, dy

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distanceToPoint(self, target):
        dx, dy = self.__getDxDy(target)

        dist = (dx**2 + dy**2) ** 0.5
        return dist

    def halfway(self, target):
         mx = (self.x + target.x) / 2
         my = (self.y + target.y) / 2
         return Point(mx, my)

    def slopeToPoint(self, target):
        dx, dy = self.__getDxDy(target)

        return dy/dx

    def getEq(self, target):
        a = self.slopeToPoint(target)
        b = target.y - a * target.x

        return a, b


p1 = Point(3, 4)
p2 = Point(4, 10)
origin = Point(0, 0)

print(p1)
print(p1.distanceFromOrigin())
print(p1.distanceToPoint(Point(5, 4)))
print(p2.slopeToPoint(origin))
print(Point(4, 11).getEq(Point(6, 15)))
print(Point(-2, 6).getEq(Point(-10, -6)))