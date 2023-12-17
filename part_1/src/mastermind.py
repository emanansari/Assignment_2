import random


class CodeMaker:
    def __init__(self):
        self.valid_symbols = ['W', 'B', 'Y', 'G', 'R', 'X']
        self.secret_code = self.generate_code()

    def code_generation(self):
        return [random.choice(self.valid_symbols) for _ in range(4)]
