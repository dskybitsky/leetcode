import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import Dict, List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        return

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_nextPermutation(self):
        solution = Solution()

        nums = [1,2,3]

        solution.nextPermutation(nums)

        self.assertEqual(nums, [1, 3, 2])

        nums = [3,2,1]

        solution.nextPermutation(nums)

        self.assertEqual(nums, [1, 2, 3])

        nums = [1,1,5]

        solution.nextPermutation(nums)

        self.assertEqual(nums, [1, 5, 1])


if __name__ == '__main__':
    unittest.main()
