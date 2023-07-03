from typing import List
import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        i1 = 0
        i2 = n

        while i1 < i2:
            i_mid = i1 + (i2 - i1) // 2

            if matrix[i_mid][0] < target:
                i1 = i_mid + 1
            elif matrix[i_mid][0] > target:
                i2 = i_mid
            else:
                return True
        
        if i1 == 0:
            return False
        
        i_trgt = i1 - 1

        j_trgt = bisect.bisect_left(matrix[i_trgt], target)

        if j_trgt < m and matrix[i_trgt][j_trgt] == target:
            return True

        return False


sol = Solution()

assert sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3) is True
assert sol.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13) is False