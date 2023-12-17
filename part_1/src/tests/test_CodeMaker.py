import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'part_1/src'))
from mastermind import CodeMaker


class TestCodeMaker(unittest.TestCase):
    def setUp(self):
        self.code_maker = CodeMaker()
        self.valid_symbols = ['W', 'B', 'Y', 'G', 'R', 'X']

    def test_code_generation(self):
        code = self.code_maker.generate_code()
        self.assertEqual(len(code), 4)

    def test_feedback_accuracy(self):
        code_maker = CodeMaker()
        code_maker.code = ['R', 'G', 'B', 'Y']
        guess = ['R', 'G', 'B', 'Y']
        feedback = code_maker.provide_feedback(guess)
        expected_feedback = (4, 0)
        feedback_msg = "4 correct guesses at right position, 0 at wrong."
        self.assertEqual(feedback, expected_feedback, feedback_msg)


if __name__ == '__main__':
    unittest.main()
