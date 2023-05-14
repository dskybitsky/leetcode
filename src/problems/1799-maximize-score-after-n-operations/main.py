from typing import List
from math import gcd


class Solution:
    def backtrack(self, nums: List[int], mask: int, picked: int, memo: List[int]) -> int:
        n = len(nums)
        
        if 2 * picked == n:
            return 0

        if memo[mask] != -1:
            return memo[mask]

        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                if (mask >> i) & 1 == 1 or (mask >> j) & 1 == 1:
                    continue

                new_mask = mask | (1 << i) | (1 << j)

                score = (picked + 1) * gcd(nums[i], nums[j])

                next_score = self.backtrack(nums, new_mask, picked + 1, memo)

                ans = max(ans, score + next_score)
        
        memo[mask] = ans

        return ans


    def maxScore(self, nums: List[int]) -> int:
        memo = [-1] * (2 ** len(nums))
        return self.backtrack(nums, 0, 0, memo)

sol = Solution()

assert sol.maxScore([1, 2]) == 1
assert sol.maxScore([3, 4, 6, 8]) == 11
assert sol.maxScore([1, 2, 3, 4, 5, 6]) == 14

