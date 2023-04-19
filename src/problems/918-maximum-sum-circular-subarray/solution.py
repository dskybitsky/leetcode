from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n

        ans = nums[0]

        for j in range(n):
            dp[0] = nums[j]

            ans = max(ans, dp[0])

            k = 1

            for i in range(j + 1, n):
                dp[k] = max(nums[i], nums[i] + dp[k - 1])
                ans = max(ans, dp[k])
                k += 1

            for i in range(j):
                dp[k] = max(nums[i], nums[i] + dp[k - 1])
                ans = max(ans, dp[k])
                k += 1

        return ans


if __name__ == '__main__':
    sol = Solution()

    assert sol.maxSubarraySumCircular([5, -3, 5]) == 10
    assert sol.maxSubarraySumCircular([1, -2, 3, -2]) == 3
    assert sol.maxSubarraySumCircular([-3, -2, -3]) == -2
