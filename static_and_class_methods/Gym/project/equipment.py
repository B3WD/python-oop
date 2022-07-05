class Equipment:
    id = 1 # could be a problem

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    def __repr__(self) -> str:
        return f"Equipment <{self.id}> {self.name}"

    @classmethod
    def get_next_id(cls):
        temp = cls.id
        cls.id += 1
        return temp

