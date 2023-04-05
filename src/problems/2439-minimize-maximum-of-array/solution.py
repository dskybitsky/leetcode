import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import List
from math import ceil

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        i = 1

        swapped = False

        while i < len(nums):
            if nums[i - 1] < nums[i]:
                avg = ceil((nums[i - 1] + nums[i]) / 2)
                nums[i] -= (avg - nums[i - 1])
                nums[i - 1] = avg
                swapped = True

            i += 1

        if swapped:
            return self.minimizeArrayValue(nums)

        return nums[0]

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_minimizeArrayValue(self):
        solution = Solution()

        self.assertEqual(solution.minimizeArrayValue([13,13,20,0,8,9,9]), 16)

        self.assertEqual(solution.minimizeArrayValue([3,7,1,6]), 5)
        self.assertEqual(solution.minimizeArrayValue([10, 1]), 10)

if __name__ == '__main__':
    unittest.main()
