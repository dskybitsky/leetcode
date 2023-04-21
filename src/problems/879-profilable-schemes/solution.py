from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)

        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(m + 1)]

        for cnt in range(n + 1):
            dp[m][cnt][minProfit] = 1

        for i in range(m - 1, -1, -1):
            for cnt in range(n + 1):
                for p in range(minProfit + 1):
                    dp[i][cnt][p] = dp[i + 1][cnt][p]

                    if cnt + group[i] <= n:
                        dp[i][cnt][p] = (
                            dp[i][cnt][p] + dp[i + 1][cnt + group[i]][min(minProfit, p + profit[i])]
                        ) % 1000000007
        
    
        return dp[0][0][0]


if __name__ == '__main__':
    sol = Solution()


    assert sol.profitableSchemes(5, 3, [2, 2], [2, 3]) == 2
    assert sol.profitableSchemes(1, 1, [1, 1, 1, 1, 2, 2, 1, 2, 1, 1], [0, 1, 0, 0, 1, 1, 1, 0, 2, 2]) == 4
    assert sol.profitableSchemes(1, 1, [1], [1]) == 1
    assert sol.profitableSchemes(64, 0, [80, 40], [88, 88]) == 2
    assert sol.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]) == 7
