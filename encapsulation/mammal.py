class Mammal:
    def __init__(self, name: str, type, sound) -> None:
        self.name = name
        self.type = type
        self.sound = sound
        self.__kingdom = "mammals"

    @property
    def kingdom(self):
        return self.__kingdom

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def info(self):
        return f"{self.name} is of type {self.type}"
    

mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.kingdom)
print(mammal.info())