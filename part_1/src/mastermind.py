import random


class CodeMaker:
    def __init__(self) -> None:
        self.initials = "WRGYBX"
        self.code = self.generate_code()

    def generate_code(self):
        return ''.join(random.choice(self.initials) for _ in range(4))
