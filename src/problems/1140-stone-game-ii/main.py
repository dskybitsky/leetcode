from typing import List
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @lru_cache(maxsize=None)
        def solve(p: int = 0, i: int = 0, m: int = 1) -> int:
            if i == n:
                return 0
            
            res = 1000000 if p == 1 else -1

            s = 0

            for j in range(1, min(2 * m, n - i) + 1):
                s += piles[i + j - 1]

                if p == 0:
                    res = max(res, s + solve(1, i + j, max(m, j)))
                else:
                    res = min(res, solve(0, i + j, max(m, j)))

            return res

        return solve()


sol = Solution()

assert sol.stoneGameII(piles = [2,7,9,4,4]) == 10
assert sol.stoneGameII(piles = [1,2,3,4,5,100]) == 104