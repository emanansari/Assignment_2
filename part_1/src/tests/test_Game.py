import unittest
import os
import sys
from unittest.mock import patch
from io import StringIO
sys.path.append(os.path.join(os.getcwd(), 'part_1/src'))
from mastermind import Game, CodeBreaker, CodeMaker


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_game_initialization(self):
        self.assertIsInstance(self.game.code_maker, CodeMaker)
        self.assertIsInstance(self.game.code_breaker, CodeBreaker)
        self.assertEqual(self.game.attempts, 0)

    def test_play_round(self):
        with patch.object(CodeBreaker, 'make_guess', return_value='WRGY'), \
             patch.object(CodeMaker, 'provide_feedback', return_value=(1, 2)):
            self.game.play_round()
            self.assertEqual(self.game.attempts, 1)

    def test_game_feedback(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.game.display_feedback(1, "WRGB", (2, 1))
        expected_output = "\nAttempt #1:\nGuess: WRGB\nFeedback: (2, 1)\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
