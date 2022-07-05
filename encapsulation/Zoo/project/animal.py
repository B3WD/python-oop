class Animal:
    money_for_care = None

    def __init__(self, name: str, gender: str, age: int) -> None:
        self.name = name
        self.gender = gender
        self.age = age

    def __repr__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    @classmethod
    def get_needs(cls):
        return cls.money_for_care 