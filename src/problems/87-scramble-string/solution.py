import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from functools import lru_cache

class Solution:
    
    @lru_cache(maxsize=None)
    def isScramble(self, s1: str, s2: str) -> bool:
        s1Len = len(s1)

        if s1Len != len(s2):
            return False

        if s1 == s2:
            return True

        if s1Len == 2 and s1[0] == s2[1] and s1[1] == s2[0]:
            return True

        for i in range(1, s1Len):
            if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]):
                return True

        return False

###############################################################################

if __name__ == "__main__":
    solution = Solution()

    assert solution.isScramble('great', 'rgeat')
    assert not solution.isScramble('abcde', 'caebd')
    assert solution.isScramble('a', 'a')
    assert solution.isScramble('abcdbdacbdac', 'bdacabcdbdac')
