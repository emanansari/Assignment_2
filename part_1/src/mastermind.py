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
        valid_colors = "WRGYBX"
        while True:
            guess = input("Guess! (e.g., 'WRGB'): ").upper()
            if all(color in valid_colors for
                   color in guess) and len(guess) == 4:
                return guess
            else:
                print("Guess is too long!")


class Game:
    def __init__(self):
        self.code_maker = CodeMaker()
        self.code_breaker = CodeBreaker()
        self.attempts = 0

    def play_round(self):
        self.attempts = 10

    def display_feedback(self, attempt, guess, feedback):
        print(f"\nAttempt #{attempt}:")
        print(f"Guess: {guess}")
        print(f"Feedback: {feedback}")
