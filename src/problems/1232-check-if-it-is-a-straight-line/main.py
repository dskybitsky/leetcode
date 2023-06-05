from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)

        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]

        k =  dy / dx if dx != 0 else None

        for i in range(1, n - 1):

            dx1 = coordinates[i + 1][0] - coordinates[i][0]
            dy1 = coordinates[i + 1][1] - coordinates[i][1]

            k1 =  dy1 / dx1 if dx1 != 0 else None

            if k is None and k1 is not None:
                return False
            
            if k is not None and k1 is None:
                return False
            
            if k1 != k:
                return False

        return True


sol = Solution()

assert sol.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]) is True
assert sol.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]) is False

print ("Ok")