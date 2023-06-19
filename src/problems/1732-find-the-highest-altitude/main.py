from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_h = 0
        curr_h = 0

        for h in gain:
            curr_h += h
            max_h = max(max_h, curr_h)

        return max_h


sol = Solution()

assert sol.largestAltitude(gain = [-5,1,5,0,-7]) == 1