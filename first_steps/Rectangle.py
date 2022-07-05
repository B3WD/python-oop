from Point import Point


class Rectangle:

    def __init__(self, p, w, h):
        self.CornerPoint = p
        self.width = w
        self.height = h

    def __str__(self):
        return f"Rectangle {self.width} by {self.height}, at {self.CornerPoint}."

    def transpose(self):
        self.width, self.height = self.height, self.width

    @property
    def diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def contains(self, p):
        x_bound = self.CornerPoint.x + self.width
        y_bound = self.CornerPoint.y + self.height

        if self.CornerPoint.x <= p.x <= x_bound and self.CornerPoint.y <= p.y <= y_bound:
            return True
        else:
            return False
    
    @property
    def corners(self):
        cornersLst = []

        cornersLst.append(self.CornerPoint)
        cornersLst.append(Point(self.CornerPoint.x + self.width, self.CornerPoint.y))
        cornersLst.append(Point(self.CornerPoint.x + self.width, self.CornerPoint.y + self.height))
        cornersLst.append(Point(self.CornerPoint.x, self.CornerPoint.y + self.height))

        return cornersLst

    def P(self):
        return 2 * (self.width + self.height)

    def S(self):

        return self.width * self.height

    def isColliding(self, target):

        for corner in target.corners:
            if self.contains(corner):
                return True

        return False


def t1():
    r1 = Rectangle(Point(3, 4), 5, 6)
    print(r1)
    print(r1.P())
    print(r1.S())

    r1.transpose()

    print(r1)
    print(r1.diagonal)

def t2():

    r = Rectangle(Point(0, 0), 10, 5)
    r.contains(Point(0, 0)), #True
    r.contains(Point(3, 3)), #True
    r.contains(Point(3, 7)), #False
    r.contains(Point(3, 5)), #False
    r.contains(Point(3, 4.99999)), #True
    r.contains(Point(-3, -3)), #False

    print(r.diagonal)

def t3():
    r = Rectangle(Point(0, 0), 1, 1)
    r.contains(Point(0, 0))
    r.contains(Point(1, 0))
    r.contains(Point(0, 1))
    r.contains(Point(1, 1))

    [print(corner) for corner in r.corners]

def t3():
    r = Rectangle(Point(0, 0), 3, 3) #True
    
    [print(corner) for corner in r.corners]

def t4():
    r = Rectangle(Point(0, 0), 3, 3) #True
    k = Rectangle(Point(0, 0), 3, 3) #True
    s = Rectangle(Point(-2, 2), 3, 3) #True
    t = Rectangle(Point(3, 3), 3, 3) #True
    p = Rectangle(Point(-2, 2), 3, 3) #True
    v = Rectangle(Point(-2, -2), 1, 1) #False

    rects = [k, s, t, p, v]

    for rect in rects:
        print(r.isColliding(rect))

def main():
    #t1()
    #t2()
    #t3()
    t4()

if __name__ == "__main__":
    main()