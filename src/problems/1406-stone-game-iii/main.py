from typing import List
from functools import lru_cache


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @lru_cache(maxsize=None)
        def f(p: int = 0, i: int = 0) -> int:
            if i >= n:
                return 0

            res = -1000

            s = 0

            for j in range(1, min(3, n - i) + 1):
                s += stoneValue[i + j - 1]

                if p == 0:
                    res = max(res, s - f(1, i + j))
                else:
                    res = max(res, s - f(0, i + j))
            
            return res

        res = f()

        if res > 0:
            return "Alice"
        
        if res < 0:
            return "Bob"

        return "Tie"


sol = Solution()

assert sol.stoneGameIII([1,2,3,7]) == "Bob"
assert sol.stoneGameIII([1,2,3,-9]) == "Alice"
assert sol.stoneGameIII([1,2,3,6]) == "Tie"

print("OK")