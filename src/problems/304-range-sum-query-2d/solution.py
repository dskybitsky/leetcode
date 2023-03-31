import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        return

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return 0

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_ways(self):
        matri = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])

        self.assertEqual(numMatrix.sumRegion(2, 1, 4, 3), 8)
        self.assertEqual(numMatrix.sumRegion(1, 1, 2, 2), 11)
        self.assertEqual(numMatrix.sumRegion(1, 2, 2, 4), 12)

if __name__ == '__main__':
    unittest.main()
