import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        return []

###############################################################################

import unittest

class SolutionTest(unittest.TestCase):
    def test_findSubstring(self):
        solution = Solution()

        self.assertEqual(solution.findSubstring("barfoothefoobarman", ["foo","bar"]), [0, 9])
        self.assertEqual(solution.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]), [])
        self.assertEqual(solution.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]), [6, 9, 12])

if __name__ == '__main__':
    unittest.main()
