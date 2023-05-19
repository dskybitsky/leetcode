from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = { }

        ans = 0

        n = len(nums)

        for i in range(n):
            dp[0] = { nums[i]: 1 }

            for j in range(i):
                diff = nums[i] - nums[j]

                if diff not in dp:
                    dp[diff] = { nums[i]: 2}
                elif nums[j] in dp[diff]:
                    dp[diff][nums[i]] = dp[diff][nums[j]] + 1
                else:
                    dp[diff][nums[i]] = 1

                ans = max(ans, dp[diff][nums[i]])
        
        return ans
    

sol = Solution()

assert sol.longestArithSeqLength([3, 6, 9, 12]) == 4
assert sol.longestArithSeqLength([9, 4, 7, 2, 10]) == 3
assert sol.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]) == 4
