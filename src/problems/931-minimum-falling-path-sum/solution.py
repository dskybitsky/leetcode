from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        max_num = 10001

        for i in range(1, n):
            for j in range(m):
                matrix[i][j] += min(
                    matrix[i - 1][j - 1] if j > 0 else max_num,
                    matrix[i - 1][j],
                    matrix[i - 1][j + 1] if j < n - 1 else max_num
                )

        return min(matrix[n - 1])
    

if __name__ == '__main__':
    sol = Solution()

    assert sol.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
    assert sol.minFallingPathSum([[-19, 57], [-40, -5]]) == -59