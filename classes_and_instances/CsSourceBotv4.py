# Idea: Each bot should habe its alive state, but
# also I want a way to kill them all without iterating
# over all bots, and manually changing their state.

# Also a really bad implementation

class CsSourceBot:
    id = 0
    alive = True
    
    def __init__(self, name = "Alex", hp = 100):
        self.id = self.get_id()
        self.name = f"{name}_{self.id}"
        self.alive = True

    @staticmethod
    def kill_all():
        CsSourceBot.alive = False

    def get_id(self):
        CsSourceBot.id += 1
        return CsSourceBot.id

    def kill(self):
        self.alive = False

    def __str__(self) -> str:
        if not CsSourceBot.alive:
            self.alive = CsSourceBot.alive

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
b3.kill()

print("======")
print(b1)
print(b2)
print(b3)
print(b4)

CsSourceBot.kill_all()

print("===Kill all===")
print(b1)
print(b2)
print(b3)
print(b4)