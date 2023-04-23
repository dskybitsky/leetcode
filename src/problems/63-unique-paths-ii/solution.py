from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(1, n):
            if dp[0][i - 1] == 0:
                break
            dp[0][i] = dp[0][i - 1] if obstacleGrid[0][i] == 0 else 0

        for i in range(1, m):
            if dp[i - 1][0] == 0:
                break
            dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0

        for i in range(1, m):
            all_zeros = True

            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = 0

                if dp[i][j] > 0:
                    all_zeros = False

            if i < m - 1 and dp[i + 1][0] == 0 and all_zeros:
                break

        return dp[m - 1][n - 1]


if __name__ == '__main__':
    sol = Solution()

    assert sol.uniquePathsWithObstacles([[0],[0]])

    assert sol.uniquePathsWithObstacles(
        [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]
    ) == 10
    assert sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert sol.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1
