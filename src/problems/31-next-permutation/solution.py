import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import Dict, List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        total = len(nums)

        for i in range(total - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                    nums[i:] = sorted(nums[i:])

                    for j in range(i, total):
                        if nums[i - 1] < nums[j]:
                            self.swap(nums, i - 1, j)
                            return
    
        nums.sort()

    def swap(self, nums: List[int], i: int, j: int) -> None:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    
    def test_nextPermutation_c(self):
        solution = Solution()
        
        nums = [4,2,0,2,3,2,0]

        solution.nextPermutation(nums)

        self.assertEqual(nums, [4,2,0,3,0,2,2])

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

        self.assertEqual(nums, [2, 1, 3])

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
