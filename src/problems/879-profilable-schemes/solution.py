from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        return 0


if __name__ == '__main__':
    sol = Solution()

    assert sol.profitableSchemes(5, 3, [2, 2], [2, 3]) == 2
    assert sol.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]) == 2
