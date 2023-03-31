import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import List

class Solution:
    def ways(self, pizza: List[str], k: int, top = 0, left = 0) -> int:
        if top == len(pizza) or left == len(pizza[0]):
            return 0

        if not self.containsApple(pizza, top, left, len(pizza), len(pizza[0])):
            return 0

        if k == 1:
            return 1

        result = 0

        for i in range(top + 1, len(pizza)):
            if self.containsApple(pizza, top, left, i, len(pizza[0])):
                result += self.ways(pizza, k - 1, i, left)

        for i in range(left + 1, len(pizza[0])):
            if self.containsApple(pizza, top, left, len(pizza), i):
                result += self.ways(pizza, k - 1, top, i)

        return result

    def containsApple(self, pizza: List[str], top: int, left: int, bottom: int, right: int) -> bool:
        for i in range(top, bottom):
            if "A" in pizza[i][left:right]:
                return True

        return False

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_containsApple(self):
        solution = Solution()

        self.assertEqual(solution.containsApple(["AA",".."], 0, 0, 2, 2), True)
        self.assertEqual(solution.containsApple(["AA",".."], 1, 0, 2, 2), False)
        self.assertEqual(solution.containsApple(["AA",".."], 0, 1, 2, 2), True)
        self.assertEqual(solution.containsApple(["AA",".."], 1, 1, 2, 2), False)


    def test_ways(self):
        solution = Solution()

        self.assertEqual(solution.ways(["AAA","..."], 2), 2)
        self.assertEqual(solution.ways(["..","AA",".."], 2), 1)
        
        self.assertEqual(solution.ways(["A..","AAA","..."], 3), 3)

        self.assertEqual(solution.ways(["A..","AA.","..."], 3), 1)
        self.assertEqual(solution.ways(["A..","A..","..."], 1), 1)

if __name__ == '__main__':
    unittest.main()
