from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)

        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if arr[i] == arr[j] + difference:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


sol = Solution()

assert sol.longestSubsequence([1, 2, 3, 4], 1) == 4
assert sol.longestSubsequence([1, 3, 5, 7], 1) == 1
assert sol.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
