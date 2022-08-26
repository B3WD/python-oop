class Foo:
    def __init__(self, x) -> None:
        self.x = x

    def method(self, arg):
        print(f"{self.x} {arg}")


class Bar:
    def  __init__(self, x) -> None:
        self.x = x


class Baz(Foo):
    def __init__(self, x) -> None:
        super().__init__(x)


class Qux(Foo):
    def __init__(self, x) -> None:
        Foo.__init__(self, x)  # same logic as: Foo.method(bar, "Baz")
                               # also is unbound method


# bound method
foo = Foo("Foo")
foo.method("Fop")

# unbound method
bar = Bar("Bar")
Foo.method(bar, "Baz")

qux = Qux("Qux")
qux.method("Qut")