from typing import List


class Solution:
    def find(
        self,
        index: int,
        count: int,
        profit: int,
        n: int,
        minProfit: int,
        group: List[int],
        profits: List[int]
    ) -> int:
        if index == len(group):
            return 1 if profit >= minProfit else 0
        
        if self.memo[index][count][profit] != -1:
            return self.memo[index][count][profit]

        res = self.find(index + 1, count, profit, n, minProfit, group, profits)

        if count + group[index] <= n:
            res += self.find(index + 1, count + group[index], min(minProfit, profit + profits[index]), n, minProfit, group, profits)

        self.memo[index][count][profit] = res % 1000000007

        return self.memo[index][count][profit]

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profits: List[int]) -> int:
       self.memo = [ [ [-1] * (minProfit + 1) for _ in range(n + 1)] for _ in range(len(group) + 1)]

       return self.find(0, 0, 0, n, minProfit, group, profits)


if __name__ == '__main__':
    sol = Solution()


    assert sol.profitableSchemes(5, 3, [2, 2], [2, 3]) == 2
    assert sol.profitableSchemes(1, 1, [1, 1, 1, 1, 2, 2, 1, 2, 1, 1], [0, 1, 0, 0, 1, 1, 1, 0, 2, 2]) == 4
    assert sol.profitableSchemes(1, 1, [1], [1]) == 1
    assert sol.profitableSchemes(64, 0, [80, 40], [88, 88]) == 2
    assert sol.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]) == 7
