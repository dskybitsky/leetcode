import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import List
from functools import cache
from math import floor

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []

        totalPotions = len(potions)

        potions.sort()

        for i in range(len(spells)):
            target = success / spells[i];

            firstSuccPotion = self.findFirstGreaterOrEqual(potions, target)

            ans.append(totalPotions - firstSuccPotion if firstSuccPotion >= 0 else 0)

        return ans

    def findFirstGreaterOrEqual(self, nums: List[int], target: float) -> int:
        left = 0
        right = len(nums) - 1

        if right < 0:
            return -1

        while (left <= right):
            if left == right:
                return left if nums[left] >= target else -1

            mid = left + floor((right - left) / 2)

            if nums[mid] < target:
                left = mid + 1
            else:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                else:
                    right = mid - 1
        return -1


###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_findFirstGreaterOrEqual(self):
        solution = Solution()
        
        self.assertEqual(solution.findFirstGreaterOrEqual([], 0), -1)

        self.assertEqual(solution.findFirstGreaterOrEqual([1], 0), 0)
        self.assertEqual(solution.findFirstGreaterOrEqual([1], 0.5), 0)

        self.assertEqual(solution.findFirstGreaterOrEqual([1, 2], 0), 0)
        self.assertEqual(solution.findFirstGreaterOrEqual([1, 2], 0.1), 0)
        self.assertEqual(solution.findFirstGreaterOrEqual([1, 2], 1), 0)
        self.assertEqual(solution.findFirstGreaterOrEqual([1, 2], 1.5), 1)
        self.assertEqual(solution.findFirstGreaterOrEqual([1, 2], 2.5), -1)

        self.assertEqual(solution.findFirstGreaterOrEqual([1, 2, 3], 0), 0)
        self.assertEqual(solution.findFirstGreaterOrEqual([1, 2, 3], 0.5), 0)
        self.assertEqual(solution.findFirstGreaterOrEqual([1, 2, 3], 1), 0)
        self.assertEqual(solution.findFirstGreaterOrEqual([1, 2, 3], 1.5), 1)
        self.assertEqual(solution.findFirstGreaterOrEqual([1, 2, 3], 2.5), 2)
        self.assertEqual(solution.findFirstGreaterOrEqual([1, 2, 3], 3), 2)
        self.assertEqual(solution.findFirstGreaterOrEqual([1, 2, 3], 3.1), -1)

    def test_successfulPairs(self):
        solution = Solution()

        self.assertEqual(
            solution.successfulPairs([5,1,3], [1,2,3,4,5], 7),
            [4, 0, 3]
        )

if __name__ == '__main__':
    unittest.main()
