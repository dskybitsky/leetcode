from typing import List
import bisect


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1] * n
        cnt = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]

        max_len = max(dp)
        ans = 0

        for i in range(n):
            if dp[i] == max_len:
                ans += cnt[i]

        return ans


if __name__ == "__main__":
    sol = Solution()

    assert sol.findNumberOfLIS([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 10
    assert sol.findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]) == 3
    assert sol.findNumberOfLIS([3, 2, 1]) == 3
    assert sol.findNumberOfLIS([2, 2, 2, 2, 2]) == 5
    assert sol.findNumberOfLIS([3, 1, 2]) == 1
    assert sol.findNumberOfLIS([1, 3, 5, 4, 7]) == 2

    print("OK")