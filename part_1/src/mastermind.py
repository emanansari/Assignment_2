import random


class CodeMaker:
    def __init__(self) -> None:
        self.initials = "WRGYBX"
        self.code = self.generate_code()

    def generate_code(self):
        return ''.join(random.choice(self.initials) for _ in range(4))

    def provide_feedback(self, guess):
        correct_position = sum(g == c for g, c in zip(guess, self.code))
        correct_colors_wrong_positions = 0
        code_copy = list(self.code)
        guess_copy = list(guess)

        for i in range(len(guess)):
            if guess[i] == self.code[i]:
                code_copy[i] = None
                guess_copy[i] = None

        for color in guess_copy:
            if color and color in code_copy:
                correct_colors_wrong_positions += 1
                code_copy[code_copy.index(color)] = None

        return correct_position, correct_colors_wrong_positions


class CodeBreaker:
    def __init__(self) -> None:
        self.guesses = []

    def make_guess(self):
        while True:
            guess = input("Guess! (e.g., 'WRGB'): ").upper()
            if len(guess) == 4:
                self.guesses.append(guess)
                return guess
            else:
                print("Guess is too long!")


class Game:
    pass
