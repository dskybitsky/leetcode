import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import Dict, List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp

                return
        
        nums.sort()

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_nextPermutation_2(self):
        solution = Solution()

        nums = [1,2]

        solution.nextPermutation(nums)

        self.assertEqual(nums, [2, 1])

        solution.nextPermutation(nums)

        self.assertEqual(nums, [1, 2])

    def test_nextPermutation_3(self):
        solution = Solution()

        nums = [1,2,3]

        solution.nextPermutation(nums)

        self.assertEqual(nums, [1, 3, 2])

        solution.nextPermutation(nums)

        self.assertEqual(nums, [2, 3, 1])

        solution.nextPermutation(nums)

        self.assertEqual(nums, [3, 1, 2])

        solution.nextPermutation(nums)

        self.assertEqual(nums, [3, 2, 1])

        solution.nextPermutation(nums)

        self.assertEqual(nums, [1, 2, 3])

    def test_nextPermutation_dup(self):
        solution = Solution()

        nums = [1,1,5]

        solution.nextPermutation(nums)

        self.assertEqual(nums, [1, 5, 1])

        solution.nextPermutation(nums)

        self.assertEqual(nums, [5, 1, 1])

        solution.nextPermutation(nums)

        self.assertEqual(nums, [1, 1, 5])


if __name__ == '__main__':
    unittest.main()
