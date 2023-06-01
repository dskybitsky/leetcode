from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] != 0:
            return -1
        
        grid[0][0] = -1

        to_visit = [(0, 0)]
        
        while len(to_visit) > 0:
            vi, vj = to_visit.pop(0)

            d = grid[vi][vj]

            for ni in range(max(vi - 1, 0), min(vi + 1, n - 1) + 1):
                for nj in range(max(vj - 1, 0), min(vj + 1, n - 1) + 1):
                    if grid[ni][nj] == 0 or grid[ni][nj] < 0 and grid[ni][nj] < (d - 1):
                        to_visit.append((ni, nj))
                        grid[ni][nj] = d - 1
        
        return -grid[n - 1][n - 1] if grid[n - 1][n - 1] < 0 else -1


sol = Solution()
assert sol.shortestPathBinaryMatrix([[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]) == 14
assert sol.shortestPathBinaryMatrix(grid = [[0,1],[1,0]]) == 2
assert sol.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]]) == 4
assert sol.shortestPathBinaryMatrix(grid = [[1,0,0],[1,1,0],[1,1,0]]) == -1