from typing import List
import bisect


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)

        dp = [1] * n

        hash = { }

        for i in range(n):
            diff = arr[i] - difference
            
            if diff in hash:
                for j in hash[diff]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
            if arr[i] in hash:
                hash[arr[i]].append(i)
            else:
                hash[arr[i]] = [i]

        return max(dp)


sol = Solution()

assert sol.longestSubsequence([1, 2, 3, 4], 1) == 4
assert sol.longestSubsequence([1, 3, 5, 7], 1) == 1
assert sol.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2) == 4
