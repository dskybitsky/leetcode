import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

from functools import lru_cache
from collections import Counter

class Solution:
    
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(maxsize = None)
        def isMatch(s1: str, s2: str) -> bool:
            length = len(s1)

            if s1 == s2:
                return True
                
            if Counter(s1) != Counter(s2):
                return False

            if length == 2 and s1[0] == s2[1] and s1[1] == s2[0]:
                return True
            
            for i in range(1, length):
                if (
                    isMatch(s1[0:i], s2[0:i]) and isMatch(s1[i:], s2[i:])
                    or isMatch(s1[0:i], s2[length - i:]) and isMatch(s1[i:], s2[0: length - i])
                ):
                    return True

            return False
        
        return isMatch(s1, s2)

###############################################################################

if __name__ == "__main__":
    solution = Solution()

    assert solution.isScramble('great', 'rgeat')
    assert not solution.isScramble('abcde', 'caebd')
    assert solution.isScramble('a', 'a')
    assert solution.isScramble('abcdbdacbdac', 'bdacabcdbdac')
    assert not solution.isScramble('aa', 'ab')
