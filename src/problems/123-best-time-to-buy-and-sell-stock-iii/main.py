from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp_1 = [0] * n

        min_price = prices[0]

        for i in range(1, n):
            dp_1[i] = max(dp_1[i - 1], prices[i] - min_price)
            min_price = min(min_price, prices[i])

        dp_2 = [0] * n

        max_price = prices[n - 1]

        for i in range(n - 2, -1, -1):
            dp_2[i] = max(dp_2[i + 1], max_price - prices[i])
            max_price = max(max_price, prices[i])
        
        ans = 0

        for i in range(n):
            ans = max(ans, dp_1[i] + dp_2[i])

        return ans
    

sol = Solution()

assert sol.maxProfit([3,3,5,0,0,3,1,4]) == 6
assert sol.maxProfit([1,2,3,4,5]) == 4
