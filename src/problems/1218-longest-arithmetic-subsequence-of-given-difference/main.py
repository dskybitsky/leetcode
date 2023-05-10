from typing import List
import bisect


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)

        dp = { }

        ans = 0

        for num in arr:
            num_diff = num - difference

            if num_diff in dp:
                dp[num] = dp[num_diff] + 1
            else:
                dp[num] = 1
            
            ans = max(ans, dp[num])
        
        return ans


sol = Solution()

assert sol.longestSubsequence([1, 2, 3, 4], 1) == 4
assert sol.longestSubsequence([1, 3, 5, 7], 1) == 1
assert sol.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
