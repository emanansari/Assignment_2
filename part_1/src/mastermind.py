import random


class CodeMaker:
    def __init__(self) -> None:
        self.initials = "WRGYBX"
        self.code = self.generate_code()

    def generate_code(self):
        return ''.join(random.choice(self.initials) for _ in range(4))

    def provide_feedback(self, guess):
        correct_positions = sum(g == c for g, c in zip(guess, self.code))
        code_copy = list(self.code)

        for i, color in enumerate(guess):
            if color == self.code[i]:
                code_copy[i] = None
        correct_colors_wrong_positions = 0
        for i, color in enumerate(guess):
            if color in code_copy:
                correct_colors_wrong_positions += 1
                code_copy[code_copy.index(color)] = None
        return correct_positions, correct_colors_wrong_positions


class CodeBreaker:
    pass


class Game:
    pass
