from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = { }

        ans = 0

        n = len(nums)

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]

                if i not in dp:
                    dp[i] = { diff: 1 }
                
                if diff not in dp[i]:
                    dp[i][diff] = 1

                if j not in dp:
                    dp[j] = { diff: 1 }
                
                if diff not in dp[j]:
                    dp[j][diff] = 1
                
                dp[i][diff] = dp[j][diff] + 1

                ans = max(ans, dp[i][diff])
        
        return ans
    

sol = Solution()

assert sol.longestArithSeqLength([12,53,24,53,43,53,11,53,31,18]) == 4

assert sol.longestArithSeqLength([3, 6, 9, 12]) == 4
assert sol.longestArithSeqLength([9, 4, 7, 2, 10]) == 3
assert sol.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]) == 4
assert sol.longestArithSeqLength([44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28]) == 6
assert sol.longestArithSeqLength([12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18]) == 4
