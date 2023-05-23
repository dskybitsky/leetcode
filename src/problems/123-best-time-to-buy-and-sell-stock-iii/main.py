from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0
        
        ans = 0
        
        for i in range(1, n):
            l_ans = 0
            min_price = prices[0]

            for j in range(i + 1):
                l_ans = max(l_ans, prices[j] - min_price)
                min_price = min(min_price, prices[j])
            
            r_ans = 0

            if i < n - 1:
                min_price = prices[i + 1]

                for j in range(i + 1, n):
                    r_ans = max(r_ans, prices[j] - min_price)
                    min_price = min(min_price, prices[j])

            ans = max(ans, l_ans + r_ans)

        return ans
    

sol = Solution()

assert sol.maxProfit([1,2,3,4,5]) == 4
assert sol.maxProfit([3,3,5,0,0,3,1,4]) == 6
