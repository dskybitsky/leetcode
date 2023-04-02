import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import List
from functools import cache
from math import floor
from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []

        totalPotions = len(potions)

        potions.sort()

        for i in range(len(spells)):
            target = success / spells[i];

            firstSuccPotion = bisect_left(potions, target)

            ans.append(totalPotions - firstSuccPotion if firstSuccPotion >= 0 else 0)

        return ans

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_successfulPairs(self):
        solution = Solution()

        self.assertEqual(
            solution.successfulPairs([5,1,3], [1,2,3,4,5], 7),
            [4, 0, 3]
        )

if __name__ == '__main__':
    unittest.main()
