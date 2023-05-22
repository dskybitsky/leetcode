from typing import List
import bisect


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)

        envs = sorted(envelopes, key = lambda x: (x[0], x[1]))

        dp = [0] * n
        dp[0] = 1

        ans = 1

        for i in range(n):
            for j in range(i):
                if envs[i][0] > envs[j][0] and envs[i][1] > envs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                else:
                    dp[i] = max(dp[i], 1)
            
                ans = max(ans, dp[i])
        
        return ans


sol = Solution()


assert sol.maxEnvelopes([[1,15],[7,18],[7,6],[7,100],[2,200],[17,30],[17,45],[3,5],[7,8],[3,6],[3,10],[7,20],[17,3],[17,45]]) == 3
assert sol.maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]) == 4
assert sol.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]) == 3
assert sol.maxEnvelopes([[1,1],[1,1],[1,1]]) == 1