import unittest
import os
import sys
from unittest.mock import patch
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
            self.assertEqual(self.game.attempts, 10)


if __name__ == '__main__':
    unittest.main()
