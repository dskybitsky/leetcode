from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        ans = 0

        min_price = prices[0]

        for i in range(1, n):
            diff = prices[i] - min_price

            if diff > 0:
                ans += diff
                min_price = prices[i]
            else:
                min_price = min(min_price, prices[i])

        return ans


if __name__ == '__main__':
    sol = Solution()

    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0