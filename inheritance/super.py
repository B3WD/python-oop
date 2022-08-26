class Person:
    def __init__(self, name) -> None:
        self.name = name

class Student(Person):
    def __init__(self, name, uni) -> None:
        super().__init__(name)
        self.uni = uni


s = Student("Vasko", "DU")
