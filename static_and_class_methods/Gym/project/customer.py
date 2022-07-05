class Customer:
    id = 1 # this could cause some problems

    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()

    def __repr__(self) -> str:
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @classmethod
    def get_next_id(cls):
        temp = cls.id
        cls.id += 1
        return temp
