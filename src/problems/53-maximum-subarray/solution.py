from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n

        dp[0] = nums[0]

        ans = dp[0]

        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
            ans = max(ans, dp[i])

        return ans


if __name__ == '__main__':
    sol = Solution()

    assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23
