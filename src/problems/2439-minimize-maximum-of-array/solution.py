import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import List

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        return 0

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_minimizeArrayValue(self):
        solution = Solution()

        self.assertEqual(solution.minimizeArrayValue([3,7,1,6]), 5)
        self.assertEqual(solution.minimizeArrayValue([10, 1]), 10)

if __name__ == '__main__':
    unittest.main()
