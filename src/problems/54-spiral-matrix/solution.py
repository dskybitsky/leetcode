from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        ans = []

        cnt = n * m

        for w in range(-(n // -2)):
            for j in range(w, m - w):
                ans.append(matrix[w][j])
                cnt -= 1
            
            if cnt == 0:
                break
            
            for j in range(w + 1, n - w):
                ans.append(matrix[j][m - w - 1])
                cnt -= 1
            
            if cnt == 0:
                break

            for j in range(m - w - 2, w - 1, -1):
                ans.append(matrix[n - w - 1][j])
                cnt -= 1
            
            if cnt == 0:
                break

            for j in range(n - w - 2, w, -1):
                ans.append(matrix[j][w])
                cnt -= 1
            
            if cnt == 0:
                break
        
        return ans


if __name__ == "__main__":
    sol = Solution()

    assert sol.spiralOrder([[7], [9], [6]]) == [7, 9, 6]
    assert sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == (
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    )