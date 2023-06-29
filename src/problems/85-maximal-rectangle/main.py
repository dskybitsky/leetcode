from typing import List, Set, Optional
from functools import cache
import bisect

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        z_cols_dict = { }
        z_rows_dict = { }

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    if i in z_rows_dict:
                        z_rows_dict[i].add((i, j))
                    else:
                        z_rows_dict[i] = set([(i, j)])

                    if j in z_cols_dict:
                        z_cols_dict[j].add((i, j))
                    else:
                        z_cols_dict[j] = set([(i, j)])
        
        z_cols = sorted(z_cols_dict.keys())
        z_rows = sorted(z_rows_dict.keys())

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

        @cache
        def find_zero(i1: int, i2: int, j1: int, j2: int) -> Optional[List[int]]:
            r_start = bisect.bisect_left(z_rows, i1)
            r_end = bisect.bisect_right(z_rows, i2)

            z_rows_set = set()

            for r in range(r_start, r_end):
                z_rows_set.update(z_rows_dict[z_rows[r]])

            c_start = bisect.bisect_left(z_cols, j1)
            c_end = bisect.bisect_right(z_cols, j2)

            z_cols_set = set()

            for c in range(c_start, c_end):
                z_cols_set.update(z_cols_dict[z_cols[c]])

            z_set = z_rows_set & z_cols_set

            return z_set.pop() if len(z_set) else None

        return solve()


sol = Solution()

assert sol.maximalRectangle([["0"]]) == 0
assert sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 6

print("Ok")