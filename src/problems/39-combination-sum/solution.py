import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import List
from functools import cache

class Solution:
    @cache
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cnt = len(candidates)

        ans = [];

        for c in candidates:
            remain = target - c;

            if remain == 0:
                ans.append([c])
            elif remain > 0:
                nextCombs = self.combinationSum(candidates, remain)
                for comb in nextCombs:
                    comb.append(c)
                    ans.append(comb)

        return ans

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_combinationSum(self):
        solution = Solution()

        self.assertEqual(
            solution.combinationSum([2,3,6,7], 7),
            [[2,2,3],[7]]
        )
        

if __name__ == '__main__':
    unittest.main()
