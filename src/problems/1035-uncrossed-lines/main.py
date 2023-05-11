from typing import List
import bisect


class Solution:    
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n1][n2]


sol = Solution()

assert sol.maxUncrossedLines([2, 3, 1], [3, 1, 3, 3, 3, 3]) == 2
assert sol.maxUncrossedLines([3], [3, 3, 2]) == 1
assert sol.maxUncrossedLines([1, 4, 2], [1, 2, 4]) == 2
assert sol.maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]) == 3
# [2, 5, 1, 4, 3, 5, 4]
# [2, 4, 5]
assert sol.maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]) == 2
