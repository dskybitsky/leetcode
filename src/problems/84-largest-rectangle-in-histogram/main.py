from typing import List
from functools import cache

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        res = 0

        for i1 in range(n):
            
            min_h = heights[i1]

            for i2 in range(i1, n):
                min_h = min(min_h, heights[i2])

                sq = (i2 - i1 + 1) * min_h

                res = max(res, sq)

        return res



sol = Solution()

assert sol.largestRectangleArea([4,2,0,3,2,5]) == 6
assert sol.largestRectangleArea([1,1]) == 2
assert sol.largestRectangleArea([2,1,5,6,2,3]) == 10

print("Ok")