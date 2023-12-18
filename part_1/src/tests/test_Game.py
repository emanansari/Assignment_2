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
        """Test the initial setup of the game."""
        self.assertIsInstance(self.game.code_maker, CodeMaker)
        self.assertIsInstance(self.game.code_breaker, CodeBreaker)
        self.assertEqual(self.game.attempts, 0)


if __name__ == '__main__':
    unittest.main()