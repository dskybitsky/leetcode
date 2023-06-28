from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        def solve(i1: int = 0, i2: int = n - 1, j1: int = 0, j2: int = m - 1) -> int:
            if i2 < i1 or j2 < j1:
                return 0

            for i in range(i1, i2 + 1):
                for j in range(j1, j2 + 1):
                    if matrix[i][j] == '0':
                        return max(
                            solve(i1, i - 1, j1, j2),
                            solve(i + 1, i2, j1, j2),
                            solve(i1, i2, j1, j - 1),
                            solve(i1, i2, j + 1, j2)
                        )
            
            return (i2 - i1 + 1) * (j2 - j1 + 1)

        return solve()


sol = Solution()

assert sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 6