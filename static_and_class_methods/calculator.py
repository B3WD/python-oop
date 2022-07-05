import operator


class Calculator:
    @staticmethod
    def calc(op, initial, *args):
        res = initial
        for arg in args:
            res = op(res, arg)

        return res

    @classmethod
    def add(cls, *args):
        return cls.calc(operator.add, *args)

    @classmethod
    def multiply(cls, *args):
        return cls.calc(operator.mul, *args)

    @classmethod
    def divide(cls, *args):
        return cls.calc(operator.truediv, *args)

    @classmethod
    def subtract(cls, *args):
        return cls.calc(operator.sub, *args)

print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
