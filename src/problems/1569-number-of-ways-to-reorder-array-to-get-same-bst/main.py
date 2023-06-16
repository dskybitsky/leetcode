from typing import List
from math import comb


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7

        def dfs(nums) -> int:
            n = len(nums)

            if n < 3:
                return 1

            root = nums[0]
            left = []
            right = []

            for i in range(1, n):
                num = nums[i]
                
                if num < root:
                    left.append(num)
                else:
                    right.append(num)

            return dfs(left) * dfs(right) * comb(n - 1, len(left)) % mod

        return (dfs(nums) - 1) % mod


sol = Solution()

assert sol.numOfWays([2,1,3]) == 1
assert sol.numOfWays([3,4,5,1,2]) == 5
assert sol.numOfWays([1,2,3]) == 0