import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'part_1/src'))
from mastermind import CodeBreaker


class TestCodeBreaker(unittest.TestCase):
    def test_init(self):
        code_breaker = CodeBreaker()
        self.assertEqual(code_breaker.guesses, [])


if __name__ == '__main__':
    unittest.main()
