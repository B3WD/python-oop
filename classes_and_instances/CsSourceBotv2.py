# Idea: Each bot should habe its alive state, but
# also I want a way to kill them all without iterating
# over all bots, and manually changing their state.
# Reaaaaally implementation, but what to try it out.

# Maybe it would be a better idea to have a team class
# which has two child classes TeamAlive and TeamDead
# and we shuffle the bots between these objects.

class CsSourceBot:
    id = 0
    alive = True

    def kill_all():
        CsSourceBot.alive = False

    def __init__(self, name = "Alex", hp = 100):
        self.id = self.get_id()
        self.name = f"{name}_{self.id}"

    def get_id(self):
        CsSourceBot.id += 1
        return CsSourceBot.id

    def kill(self):
        self.__class__ = CsSourceBotDead

    def __str__(self) -> str:
        return f"{self.name} | alive: {CsSourceBot.alive}"

class CsSourceBotDead(CsSourceBot):
    alive = False

    def __str__(self) -> str:
        return f"{self.name} | alive: {CsSourceBotDead.alive}"



b1 = CsSourceBot()
b2 = CsSourceBot()
b3 = CsSourceBot()
b4 = CsSourceBot()
b5 = CsSourceBotDead()

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