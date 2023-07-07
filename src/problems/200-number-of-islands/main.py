from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        visited = set()

        res = 0

        def bfs(i: int, j: int):
            to_visit = [(i, j)]

            while len(to_visit):
                cell = to_visit.pop(0)

                i1, j1 = cell[0], cell[1]

                if i1 > 0 and grid[i1 - 1][j1] == '1' and (i1 - 1, j1) not in visited:
                    to_visit.append((i1 - 1, j1))

                if i1 < n - 1 and grid[i1 + 1][j1] == '1' and (i1 + 1, j1) not in visited:
                    to_visit.append((i1 + 1, j1))

                if j1 > 0 and grid[i1][j1 - 1] == '1' and (i1, j1 - 1) not in visited:
                    to_visit.append((i1, j1 - 1))

                if j1 < m - 1 and grid[i1][j1 + 1] == '1' and (i1, j1 + 1) not in visited:
                    to_visit.append((i1, j1 + 1))
                
                visited.add((i1, j1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    res += 1
        
        return res
    

sol = Solution()

assert sol.numIslands(
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
) == 1

assert sol.numIslands(
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
) == 3