from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        for i in range(1, n):
            m = len(triangle[i])

            triangle[i][0] += triangle[i - 1][0]
            triangle[i][m - 1] += triangle[i - 1][m - 2]

            for j in range(1, m - 1):
                triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])

        return min(triangle[n - 1])
    

if __name__ == '__main__':
    sol = Solution()

    assert sol.minimumTotal([[2], [3, 4], [6,5,7], [4, 1, 8, 3]]) == 11
    assert sol.minimumTotal([[-10]]) == -10
