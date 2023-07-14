from typing import List


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            if i == 0 or dp[i] > 0:
                for j in range(i + 1, n):
                    if abs(nums[i] - nums[j]) <= target:
                        dp[j] = max(dp[j], dp[i] + 1)

        return dp[n - 1] if dp[n - 1] > 0 else -1


sol = Solution()

assert sol.maximumJumps(nums = [1,3,6,4,1,2], target = 2) == 3
assert sol.maximumJumps(nums = [1,3,6,4,1,2], target = 3) == 5
assert sol.maximumJumps(nums = [1,3,6,4,1,2], target = 0) == -1