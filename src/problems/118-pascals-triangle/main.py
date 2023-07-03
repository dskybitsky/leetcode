from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        grid = []

        grid.append([1])

        for i in range(1, numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = grid[i - 1][j - 1] + grid[i - 1][j]
                
            grid.append(row)

        return grid


sol = Solution()

assert sol.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]