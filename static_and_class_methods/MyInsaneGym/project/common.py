@classmethod
def get_next_id(cls):
    temp = cls.id
    cls.id += 1
    return temp


def default_init(self, *args):
    attributes = self.__annotations__
    for (attr, value) in zip(attributes, args):
        setattr(self, attr, value)

    self.id = self.get_next_id()


def dataclass(attrs: dict(), repr_format):

    def repr_implementation(self):
        return repr_format.format(self=self)

    klass = type("_", (), attrs)
    klass.__init__ = default_init
    klass.__repr__ = repr_implementation
    klass.__annotations__ = attrs
    klass.id = 1
    klass.get_next_id = get_next_id

    return klass