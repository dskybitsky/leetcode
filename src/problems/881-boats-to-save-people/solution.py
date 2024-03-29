import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0

        people.sort(reverse = True)

        left = 0
        right = len(people) - 1

        while left <= right:
            rem = limit - people[left]

            left += 1

            if left <= right and people[right] <= rem:
                right -= 1

            ans += 1

        return ans

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_numRescueBoats(self):
        solution = Solution()

        self.assertEqual(solution.numRescueBoats([1, 2], 3), 1)
        self.assertEqual(solution.numRescueBoats([3, 2, 2, 1], 3), 3)

if __name__ == '__main__':
    unittest.main()
