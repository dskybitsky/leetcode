from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        ans = 0

        min_price = prices[0]

        for i in range(1, n):
            ans = max(ans, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return ans


if __name__ == '__main__':
    sol = Solution()

    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0