from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        res = 0

        i = m - 1

        j = 0

        while j < n:
            while grid[i][j] < 0 and i >= 0:
                res += n - j
                i -= 1
            
            j += 1
        
        return res


sol = Solution()

assert sol.countNegatives([[7,-3]]) == 1
assert sol.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]) == 8
assert sol.countNegatives([[3,2],[1,0]]) == 0