from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        rows = { }

        for i in range(n):
            row = tuple(grid[i])

            rows[row] = rows[row] + 1 if row in rows else 1

        cols = { }

        for i in range(n):
            vals = []

            for j in range(n):
                vals.append(grid[j][i])

            col = tuple(vals)

            cols[col] = cols[col] + 1 if col in cols else 1

        res = 0

        for row in rows:
            if row in cols:
                res += rows[row] * cols[row]

        return res


sol = Solution()

assert sol.equalPairs([[13,13],[13,13]]) == 4
assert sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]]) == 1
assert sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3
