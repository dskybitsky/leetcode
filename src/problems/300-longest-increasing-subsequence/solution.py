from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        inf = 10001

        dp = [inf] * (n + 1)

        dp[0] = -inf

        ans = 0

        for i in range(n):
            l = bisect.bisect_right(dp, nums[i])

            if dp[l - 1] < nums[i] and nums[i] < dp[l]:
                dp[l] = nums[i]
                ans = max(ans, l)

        return ans


if __name__ == "__main__":
    sol = Solution()

    assert sol.lengthOfLIS([0]) == 1
    assert sol.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
    assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert sol.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1