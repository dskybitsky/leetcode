from typing import List

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        mod = 10 ** 9 + 7
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        dp = [[1] * n for _ in range(m)]

        cell_list = [[i, j] for i in range(m) for j in range(n)]
        cell_list.sort(key = lambda x: grid[x[0]][x[1]])

        res = 0

        for i, j in cell_list:
            for di, dj in directions:
                curr_i, curr_j = i + di, j + dj
                if 0 <= curr_i < m and 0 <= curr_j < n and grid[curr_i][curr_j] > grid[i][j]:
                    dp[curr_i][curr_j] += dp[i][j]
                    dp[curr_i][curr_j] %= mod

            res += dp[i][j]

        return res


sol = Solution()

assert sol.countPaths([[1,1],[3,4]]) == 8
assert sol.countPaths([[1],[2]]) == 3
assert sol.countPaths([[1,1,1],[1,1,1],[1,1,1]]) == 9