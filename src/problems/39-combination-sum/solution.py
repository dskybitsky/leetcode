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
        memo = {}    

        def findCombinations(nums: List[int], target: int) -> List[List[int]]:
            if target in memo:
                return memo[target]

            ans = [];

            for c in candidates:
                remain = target - c;

                if remain == 0:
                    ans.append([c])
                elif remain > 0:
                    nextCombs = self.combinationSum(candidates, remain)
                    
                    for comb in nextCombs:
                        ans.append(comb + [c])
                else:
                    break

            memo[target] = ans

            return ans
        
        candidates.sort()

        return findCombinations(candidates, target)

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
            [[3,2,2], [7]]
        )

        self.assertEqual(
            solution.combinationSum([2,3,5], 8),
            [[2, 2, 2, 2], [3,2,2], [3, 5]]
        )
        

if __name__ == '__main__':
    unittest.main()
