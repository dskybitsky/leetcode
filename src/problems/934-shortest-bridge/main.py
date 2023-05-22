from typing import List


class Solution:
    def findIsland(self, grid: List[List[int]], n: int) -> List[int]:
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    return [i, j]
        
        return []

    def findAdjCells(self, i: int, j: int, n: int) -> List[List[int]]:
        result = []

        if i > 0:
            result.append([i - 1, j])
        
        if i < n - 1:
            result.append([i + 1, j])
        
        if j > 0:
            result.append([i, j - 1])
        
        if j < n - 1:
            result.append([i, j + 1])
        
        return result
        
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)

        i1, j1 = self.findIsland(grid, n)

        landQueue = [[i1, j1]]
        waterQueue = [[i1, j1]]
        grid[i1][j1] = 2

        while landQueue:
            nextLandQueue = []

            for i, j in landQueue:
                for i1, j1 in self.findAdjCells(i, j, n):
                    if grid[i1][j1] == 1:
                        nextLandQueue.append([i1, j1])
                        waterQueue.append([i1, j1])
                        grid[i1][j1] = 2
                
            landQueue = nextLandQueue
        
        dist = 0

        while waterQueue:
            nextWaterQueue = []

            for wi, wj in waterQueue:
                for wi1, wj1 in self.findAdjCells(wi, wj, n):
                    if grid[wi1][wj1] == 1:
                        return dist

                    if grid[wi1][wj1] == 0:
                        nextWaterQueue.append([wi1, wj1])
                        grid[wi1][wj1] = -1
                
            dist += 1

            waterQueue = nextWaterQueue

        return 0


sol = Solution()

assert sol.shortestBridge([[0,0,0,1,1],[0,0,0,1,0],[0,0,0,1,1],[0,0,1,0,1],[0,0,1,1,0]]) == 1
assert sol.shortestBridge([[0, 1], [1, 0]]) == 1
assert sol.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]) == 2
assert sol.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]) == 1

print("Ok")