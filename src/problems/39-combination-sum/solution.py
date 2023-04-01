import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import List
from functools import cache

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def solve(i: int, arr: List[List[int]], temp: List[int], target: int):
            if target == 0:
                ans.append(temp.copy())
                return

            if target < 0:
                return
            
            if i == len(arr):
                return
            
            solve(i + 1, arr, temp, target)

            temp.append(arr[i])

            solve(i, arr, temp, target - arr[i])

            temp.pop()

        temp = []

        solve(0, candidates, temp, target)

        return ans
###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_combinationSum(self):
        solution = Solution()

        self.assertEqual(
            solution.combinationSum([2,3], 5),
            [[2, 3]]
        )

        self.assertEqual(
            solution.combinationSum([2,3,6,7], 7),
            [[7], [2,2,3]]
        )

        self.assertEqual(
            solution.combinationSum([2,3,5], 8),
            [[3, 5], [2, 3, 3], [2, 2, 2, 2]]
        )
        

if __name__ == '__main__':
    unittest.main()
