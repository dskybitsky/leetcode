from typing import List
from functools import cache

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        @cache
        def solve(i1: int = 0, i2: int = n - 1) -> int:
            if i1 > i2:
                return 0
            
            sq = (i2 - i1 + 1) * mins[i1][i2]

            return max(sq, solve(i1 + 1, i2), solve(i1, i2 - 1))
        
        mins = [[None] * n for _ in range(n)]

        for i1 in range(n):
            for i2 in range(i1, n):
                mins[i1][i2] = min(mins[i1][i2 - 1], heights[i2]) if i2 > i1 else heights[i2]
        
        return solve()


sol = Solution()

assert sol.largestRectangleArea([2,1,5,6,2,3]) == 10