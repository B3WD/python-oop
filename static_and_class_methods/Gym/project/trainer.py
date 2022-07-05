class Trainer:
    id = 1

    def __init__(self, name: str) -> None:
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self) -> str:
        return f"Trainer <{self.id}> {self.name}"

    @classmethod
    def get_next_id(cls):
        temp = cls.id
        cls.id += 1
        return temp
