from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        cnt = 1
        n2 = n ** 2 + 1

        for w in range(-(n // -2)):
            for j in range(w, n - w):
                matrix[w][j] = cnt
                cnt += 1
            
            if cnt == n2:
                break
            
            for j in range(w + 1, n - w):
                matrix[j][n - w - 1] = cnt
                cnt += 1
            
            if cnt == n2:
                break

            for j in range(n - w - 2, w - 1, -1):
                matrix[n - w - 1][j] = cnt
                cnt += 1
            
            if cnt == n2:
                break

            for j in range(n - w - 2, w, -1):
                matrix[j][w] = cnt
                cnt += 1
            
            if cnt == n2:
                break
        
        return matrix



sol = Solution()

assert sol.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
assert sol.generateMatrix(1) == [[1]]