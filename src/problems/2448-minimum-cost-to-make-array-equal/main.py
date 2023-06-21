from typing import List

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)

        res = None

        for i in range(n):
            s = 0
            for j in range(n):
                s += abs(nums[i] - nums[j]) * cost[j]

            res = s if res is None else min(res, s)

        return res
    

sol = Solution()

assert sol.minCost(nums = [1,3,5,2], cost = [2,3,1,14]) == 8
assert sol.minCost(nums = [2,2,2,2,2], cost = [4,2,8,1,3]) == 0