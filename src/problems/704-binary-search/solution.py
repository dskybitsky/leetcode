import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import List
from math import floor

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if right < 0:
            return -1

        while (left <= right):
            if left == right:
                return left if nums[left] == target else -1

            mid = left + floor((right - left) / 2)

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_search(self):
        solution = Solution()
        
        self.assertEqual(solution.search([], 0), -1)
        self.assertEqual(solution.search([0], 0), 0)
        self.assertEqual(solution.search([0], 1), -1)
        self.assertEqual(solution.search([0, 1], 0), 0)
        self.assertEqual(solution.search([0, 1], 1), 1)
        self.assertEqual(solution.search([0, 1], 2), -1)
        self.assertEqual(solution.search([0, 1, 2], 0), 0)
        self.assertEqual(solution.search([0, 1, 2], 1), 1)
        self.assertEqual(solution.search([0, 1, 2], 2), 2)

if __name__ == '__main__':
    unittest.main()
