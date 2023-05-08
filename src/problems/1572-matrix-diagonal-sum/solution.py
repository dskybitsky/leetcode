from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)

        ans = 0

        for i in range(n):
            ans += mat[i][i] + mat[i][n - i - 1]

        if n % 2 == 1:
            ans -= mat[n // 2][n // 2]

        return ans


if __name__ == "__main__":
    sol = Solution()

    assert sol.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 25
    assert sol.diagonalSum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]) == 8
    assert sol.diagonalSum([[5]]) == 5