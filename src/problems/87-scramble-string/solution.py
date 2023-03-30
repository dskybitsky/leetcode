import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return False

###############################################################################

if __name__ == "__main__":
    solution = Solution()

    assert solution.isScramble('great', 'rgeat')
    assert not solution.isScramble('abcde', 'caebd')
    assert solution.isScramble('a', 'a')
