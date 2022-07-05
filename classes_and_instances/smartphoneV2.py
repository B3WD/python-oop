from dataclasses import dataclass, field
from typing import List

@dataclass
class Smartphone:
    memory: int
    apps: List[int] = field(default_factory=list)
    memory_taken: int = 0
    is_on: bool = False

    def get_left_memory(self):
        return self.memory - self.memory_taken

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if self.get_left_memory() < app_memory:
            return f"Not enough memory to install {app}"

        elif not self.is_on:
            return f"Turn on your phone to install {app}"

        self.apps.append(app)
        self.memory_taken += app_memory
        return f"Installing {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.get_left_memory()}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())