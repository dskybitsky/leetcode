from typing import List
import functools


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        @functools.lru_cache(maxsize=None)
        def solve(offset: int = 0, min_price: int = -1) -> int:
            if offset >= n:
                return 0

            if min_price < 0 or prices[offset] < min_price:
                return solve(offset + 1, prices[offset])

            res = max(
                prices[offset] - min_price - fee + solve(offset + 1),
                solve(offset + 1, min_price)
            )

            return res

        return solve()


if __name__ == '__main__':
    sol = Solution()

    assert sol.maxProfit([1, 3, 2, 8, 4, 9], 2) == 8
    assert sol.maxProfit([1, 3, 7, 5, 10, 3], 3) == 6
