from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])

        return dp[m - 1][n - 1]


if __name__ == '__main__':
    sol = Solution()

    assert sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert sol.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
