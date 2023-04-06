import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import Dict, List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        return 0

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_closedIsland(self):
        solution = Solution()

        self.assertEqual(
            solution.closedIsland(
                [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
            ),
            2
        )

        self.assertEqual(
            solution.closedIsland(
                [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
            ), 
            1
        )

        self.assertEqual(
            solution.closedIsland([
                [1,1,1,1,1,1,1],
                [1,0,0,0,0,0,1],
                [1,0,1,1,1,0,1],
                [1,0,1,0,1,0,1],
                [1,0,1,1,1,0,1],
                [1,0,0,0,0,0,1],
                [1,1,1,1,1,1,1]
            ]), 
            2
        )

if __name__ == '__main__':
    unittest.main()
