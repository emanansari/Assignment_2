import random
from typing import Tuple, List


class CodeMaker:
    def __init__(self) -> None:
        self.initials: str = "WRGYBX"
        self.code: str = self.generate_code()

    def generate_code(self) -> str:
        return ''.join(random.choice(self.initials) for _ in range(4))

    def provide_feedback(self, guess: str) -> Tuple[int, int]:
        correct_position: int = sum(g == c for g, c in zip(guess, self.code))
        correct_colors_wrong_positions: int = 0
        code_copy: List[str] = list(self.code)
        guess_copy: List[str] = list(guess)

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
        self.guesses: List[str] = []

    def make_guess(self) -> str:
        valid_colors: str = "WRGYBX"
        while True:
            guess: str = input("Guess! (e.g., 'WRGB'): ").upper()
            if all(color in valid_colors for color in guess) and len(guess) == 4:  # can you fix line too long error here
                return guess
            else:
                print("Guess is too long!")


class Game:
    MAX_ATTEMPTS: int = 10

    def __init__(self) -> None:
        self.code_maker: CodeMaker = CodeMaker()
        self.code_breaker: CodeBreaker = CodeBreaker()
        self.attempts: int = 0

    def play_round(self) -> bool:
        if self.attempts < Game.MAX_ATTEMPTS:
            self.attempts += 1
            guess: str = self.code_breaker.make_guess()
            feedback: Tuple[int, int] = self.code_maker.provide_feedback(guess)
            self.display_feedback(self.attempts, guess, feedback)

            return feedback == (4, 0)
        return False

    def play(self) -> None:
        for _ in range(Game.MAX_ATTEMPTS):
            if self.play_round():
                print("Codebreaker cracked the code! You win!")
                return
        print(f"Max attempts reached, correct code is: {self.code_maker.code}")
        print("Codebreaker loses. Better luck next time!")

    def display_feedback(self, attempt: int, guess: str,
                         feedback: Tuple[int, int]) -> None:
        print(f"\nAttempt #{attempt}:")
        print(f"Guess: {guess}")
        print(f"Feedback: {feedback}")
