from typing import List
import functools


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        hold = [0] * n
        free = [0] * n

        hold[0] = -prices[0]

        for i in range(1, n):
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)

        return free[-1]


if __name__ == '__main__':
    sol = Solution()

    assert sol.maxProfit([1, 3, 2, 8, 4, 9], 2) == 8
    assert sol.maxProfit([1, 3, 7, 5, 10, 3], 3) == 6
