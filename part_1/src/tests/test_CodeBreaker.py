import unittest
import os
import sys
from unittest.mock import patch
sys.path.append(os.path.join(os.getcwd(), 'part_1/src'))
from mastermind import CodeBreaker


class TestCodeBreaker(unittest.TestCase):
    def test_init(self):
        code_breaker = CodeBreaker()
        self.assertEqual(code_breaker.guesses, [])

    def test_make_guess_valid_length(self):
        code_breaker = CodeBreaker()
        with patch('builtins.input', side_effect=['WGRY']):
            guess = code_breaker.make_guess()
        self.assertEqual(len(guess), 4)

    def test_make_guess_valid_characters(self):
        valid_characters = "WRGYBX"
        code_breaker = CodeBreaker()
        with patch('builtins.input', side_effect=['AAAA']):
            guess = code_breaker.make_guess()
        result = all(char in valid_characters for char in guess)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
