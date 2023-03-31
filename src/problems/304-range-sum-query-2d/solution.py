import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        sumMatrix = [[0 for col in range(cols + 1)] for row in range(rows + 1)]

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                sumMatrix[row][col] = (matrix[row][col]
                    + sumMatrix[row + 1][col]
                    + sumMatrix[row][col + 1]
                    - sumMatrix[row + 1][col + 1])

        self.sumMatrix = sumMatrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.sumMatrix[row1][col1] 
            - self.sumMatrix[row2 + 1][col1] 
            - self.sumMatrix[row1][col2 + 1]
            + self.sumMatrix[row2 + 1][col2 + 1])

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_ways(self):
        numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])

        self.assertEqual(numMatrix.sumRegion(2, 1, 4, 3), 8)
        self.assertEqual(numMatrix.sumRegion(1, 1, 2, 2), 11)
        self.assertEqual(numMatrix.sumRegion(1, 2, 2, 4), 12)

if __name__ == '__main__':
    unittest.main()
