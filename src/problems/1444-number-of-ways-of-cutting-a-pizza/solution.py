import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

###############################################################################

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        return 0;


###############################################################################

if __name__ == "__main__":
    solution = Solution()

    assert solution.ways(["A..","AAA","..."], 3) == 3
    assert solution.ways(["A..","AA.","..."], 3) == 1
    assert solution.ways(["A..","A..","..."], 1) == 1