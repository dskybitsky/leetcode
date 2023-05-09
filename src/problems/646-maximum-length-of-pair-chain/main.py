from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)

        pairs = sorted(pairs, key = lambda p: p[0])

        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
    

sol = Solution()

assert sol.findLongestChain([[1, 2], [2, 3], [3, 4]]) == 2
assert sol.findLongestChain([[1, 2], [7, 8], [4, 5]]) == 3