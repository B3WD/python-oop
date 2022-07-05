class CsSourceBot:
    id = 0

    def __init__(self, name = "Alex", hp = 100):
        self.id = self.get_id()
        self.name = f"{name}_{self.id}"
        self.alive = True

    def get_id(self):
        CsSourceBot.id += 1
        return CsSourceBot.id

    def kill(self):
        self.alive = False

    def __str__(self) -> str:
        return f"{self.name} | alive: {self.alive}"


b1 = CsSourceBot()
b2 = CsSourceBot()
b3 = CsSourceBot()
b4 = CsSourceBot()

print("======")
print(b1)
print(b2)
print(b3)
print(b4)

b2.kill()

print("======")
print(b1)
print(b2)
print(b3)
print(b4)

CsSourceBot.kill()

print("======")
print(b1)
print(b2)
print(b3)
print(b4)