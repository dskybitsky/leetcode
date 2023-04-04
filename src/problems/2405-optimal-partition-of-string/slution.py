import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import List

class Solution:
    def partitionString(self, s: str) -> int:
        result = 0
        letters = set()

        for char in s:
            if char in letters:
                result += 1
                letters.clear()

            letters.add(char)

        if len(letters) > 0:
            result += 1

        return result

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_partitionString(self):
        solution = Solution()

        self.assertEqual(solution.partitionString("abacaba"), 4)
        self.assertEqual(solution.partitionString("ssssss"), 6)

if __name__ == '__main__':
    unittest.main()
