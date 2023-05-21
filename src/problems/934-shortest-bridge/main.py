from typing import List


class Solution:
    def findIsland(self, grid: List[List[int]], n: int) -> List[int]:
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    return [i, j]
        
        return []

    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)

        colors = [[None] * n for _ in range(n)]

        i1, j1 = self.findIsland(grid, n)

        toVisit = [[i1, j1]]
        toVisitNext = []

        while len(toVisit) > 0:
            i, j = toVisit.pop(0)

            colors[i][j] = 0

            if i > 0 and colors[i - 1][j] is None:
                if grid[i - 1][j] == 1:
                    toVisit.append([i - 1, j])
                else:
                    toVisitNext.append([i - 1, j, 1])
            
            if i < n - 1 and colors[i + 1][j] is None:
                if grid[i + 1][j] == 1:
                    toVisit.append([i + 1, j])
                else:
                    toVisitNext.append([i + 1, j, 1])

            if j > 0 and colors[i][j - 1] is None:
                if grid[i][j - 1] == 1:
                    toVisit.append([i, j - 1])
                else:
                    toVisitNext.append([i, j - 1, 1])
            
            if j < n - 1 and colors[i][j + 1] is None:
                if grid[i][j + 1] == 1:
                    toVisit.append([i, j + 1])
                else:
                    toVisitNext.append([i, j + 1, 1])
        
        while len(toVisitNext) > 0:
            i, j, color = toVisitNext.pop(0)

            colors[i][j] = color

            if i > 0 and colors[i - 1][j] is None:
                if grid[i - 1][j] == 1:
                    return color
            
                toVisitNext.append([i - 1, j, color + 1])
            
            if i < n - 1 and colors[i + 1][j] is None:
                if grid[i + 1][j] == 1:
                    return color

                toVisitNext.append([i + 1, j, color + 1])

            if j > 0 and colors[i][j - 1] is None:
                if grid[i][j - 1] == 1:
                    return color

                toVisitNext.append([i, j - 1, color + 1])
            
            if j < n - 1 and colors[i][j + 1] is None:
                if grid[i][j + 1] == 1:
                    return color

                toVisitNext.append([i, j + 1, color + 1])

        return 0


sol = Solution()

assert sol.shortestBridge([[0, 1], [1, 0]]) == 1
assert sol.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]) == 2
assert sol.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]) == 1

print("Ok")