import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'part_1/src'))
from mastermind import CodeMaker


class TestCodeMaker(unittest.TestCase):
    def setUp(self):
        self.code_maker = CodeMaker()
        self.valid_symbols = ['W', 'B', 'Y', 'G', 'R', 'O']

    def test_code_generation(self):
        code = self.code_maker.generate_code()
        self.assertEqual(len(code), 4)


if __name__ == '__main__':
    unittest.main()
