from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        cols = set()
        rows = set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        

sol = Solution()

matrix = [[1,1,1],[1,0,1],[1,1,1]]

sol.setZeroes(matrix)

assert matrix == [[1,0,1],[0,0,0],[1,0,1]]