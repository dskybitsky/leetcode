from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        ans = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    ans = max(ans, dp[i][j] ** 2)

        return ans


if __name__ == '__main__':
    sol = Solution()

    assert sol.maximalSquare([
        ["0", "0", "0", "1"],
        ["1", "1", "0", "1"],
        ["1", "1", "1", "1"],
        ["0", "1", "1", "1"],
        ["0", "1", "1", "1"]
    ]) == 9

    assert sol.maximalSquare([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ])  == 4

    assert sol.maximalSquare([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "1", "1", "1"]
    ])  == 9

    assert sol.maximalSquare([["0", "1"], ["1", "0"]]) == 1