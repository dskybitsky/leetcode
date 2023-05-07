from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        return []
    

if __name__ == "__main__":
    sol = Solution()

    assert sol.longestObstacleCourseAtEachPosition([1, 2, 3, 2]) == [1, 2, 3, 3]
    assert sol.longestObstacleCourseAtEachPosition([2, 2, 1]) == [1, 2, 1]
    assert sol.longestObstacleCourseAtEachPosition([3, 1, 5, 6, 4, 2]) == [1, 1, 2, 3, 2, 2]