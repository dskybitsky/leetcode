from typing import List


class Solution:
    def maxProfit(self, prices: List[int], offset: int = 0, min_price: int = -1) -> int:
        n = len(prices)

        if offset >= n:
            return 0

        if min_price < 0 or prices[offset] < min_price:
            return self.maxProfit(prices, offset + 1, prices[offset])

        return max(
            prices[offset] - min_price + self.maxProfit(prices, offset + 2),
            self.maxProfit(prices, offset + 1, min_price)
        )


if __name__ == '__main__':
    sol = Solution()

    assert sol.maxProfit([6, 1, 3, 2, 4, 7]) == 6
    assert sol.maxProfit([1, 2, 3]) == 2
    assert sol.maxProfit([1, 2, 3, 0, 2]) == 3
    assert sol.maxProfit([1]) == 0
