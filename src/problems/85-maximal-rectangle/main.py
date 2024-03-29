from typing import List, Set, Optional
from functools import cache
import bisect

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        @cache
        def solve(i1: int = 0, i2: int = n - 1, j1: int = 0, j2: int = m - 1) -> int:
            if i2 < i1 or j2 < j1:
                return 0
            
            zero = find_zero(i1, i2, j1, j2)

            if zero is None:
                return (i2 - i1 + 1) * (j2 - j1 + 1)
            
            return max(
                solve(i1, zero[0] - 1, j1, j2),
                solve(zero[0] + 1, i2, j1, j2),
                solve(i1, i2, j1, zero[1] - 1),
                solve(i1, i2, zero[1] + 1, j2)
            )
        
        dp = [[[None] * m for _ in range(n)] for _ in range(4)]
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    dp[0][i][j] = (i, j)
                    dp[1][i][j] = (i, j)
                else:
                    dp[0][i][j] = (dp[0][i - 1][j] if i > 0 else None) or (dp[0][i][j - 1] if j > 0 else None)
                    dp[1][i][j] = (dp[1][i][j - 1] if j > 0 else None) or (dp[1][i - 1][j] if i > 0 else None)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if matrix[i][j] == '0':
                    dp[2][i][j] = (i, j)
                    dp[3][i][j] = (i, j)
                else:
                    dp[2][i][j] = (dp[2][i][j + 1] if j < m - 1 else None) or (dp[2][i + 1][j] if i < n - 1 else None)
                    dp[3][i][j] = (dp[3][i + 1][j] if i < n - 1 else None) or (dp[3][i][j + 1] if j < m - 1 else None)

        def find_zero(i1: int, i2: int, j1: int, j2: int) -> Optional[List[int]]:
            dp_zeros = [
                dp[0][i2][j2],
                dp[1][i2][j2],
                dp[2][i1][j1],
                dp[3][i1][j1]
            ]

            for dp_zero in dp_zeros:
                if (
                    dp_zero is not None 
                    and dp_zero[0] >= i1 
                    and dp_zero[0] <= i2 
                    and dp_zero[1] >= j1
                    and dp_zero[1] <= j2
                ):
                    return dp_zero
            
            return None

        return solve()


sol = Solution()

assert sol.maximalRectangle([["0"]]) == 0
assert sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 6
assert sol.maximalRectangle([["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]]) == 6
assert sol.maximalRectangle([["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],["0","1","1","1","1","1"],["1","1","0","1","1","1"]]) == 8
print("Ok")