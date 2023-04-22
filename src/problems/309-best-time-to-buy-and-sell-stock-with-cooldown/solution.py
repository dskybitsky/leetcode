from typing import List
import functools


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @functools.lru_cache(maxsize=None)
        def solve(offset: int = 0, min_price: int = -1) -> int:
            if offset >= n:
                return 0

            if min_price < 0 or prices[offset] < min_price:
                return solve(offset + 1, prices[offset])

            res = max(
                prices[offset] - min_price + solve(offset + 2),
                solve(offset + 1, min_price)
            )

            return res

        return solve()


if __name__ == '__main__':
    sol = Solution()

    assert sol.maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]) == 11
    assert sol.maxProfit([6, 1, 3, 2, 4, 7]) == 6
    assert sol.maxProfit([1, 2, 3]) == 2
    assert sol.maxProfit([1, 2, 3, 0, 2]) == 3
    assert sol.maxProfit([1]) == 0
