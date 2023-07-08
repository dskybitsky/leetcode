from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        not_visited = set([(i, j) for j in range(m) for i in range(n)])

        res = 0

        def bfs(i: int, j: int):
            to_visit = [(i, j)]

            while len(to_visit):
                i1, j1 = to_visit.pop(0)

                if i1 > 0 and (i1 - 1, j1) in not_visited:
                    if grid[i1 - 1][j1] == '1':
                        to_visit.append((i1 - 1, j1))
                    
                    not_visited.remove((i1 - 1, j1))

                if i1 < n - 1 and (i1 + 1, j1) in not_visited:
                    if grid[i1 + 1][j1] == '1':
                        to_visit.append((i1 + 1, j1))
                    
                    not_visited.remove((i1 + 1, j1))

                if j1 > 0 and (i1, j1 - 1) in not_visited:
                    if grid[i1][j1 - 1] == '1':
                        to_visit.append((i1, j1 - 1))
                    
                    not_visited.remove((i1, j1 - 1))

                if j1 < m - 1 and (i1, j1 + 1) in not_visited:
                    if grid[i1][j1 + 1] == '1':
                        to_visit.append((i1, j1 + 1))
                    
                    not_visited.remove((i1, j1 + 1))

        while len(not_visited):
            i, j = not_visited.pop()

            if grid[i][j] == '1':
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