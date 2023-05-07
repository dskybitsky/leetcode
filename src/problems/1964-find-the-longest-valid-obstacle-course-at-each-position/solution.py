from typing import List
import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)

        inf = 10000001

        ans = [1] * n
        lis = []

        for i in range(n):
            idx = bisect.bisect_right(lis, obstacles[i])

            if idx == len(lis):
                lis.append(obstacles[i])
            else:
                lis[idx] = obstacles[i]
            
            ans[i] = idx + 1

        return ans


if __name__ == "__main__":
    sol = Solution()

    assert sol.longestObstacleCourseAtEachPosition([1, 2, 3, 2]) == [1, 2, 3, 3]
    assert sol.longestObstacleCourseAtEachPosition([2, 2, 1]) == [1, 2, 1]
    assert sol.longestObstacleCourseAtEachPosition([3, 1, 5, 6, 4, 2]) == [1, 1, 2, 3, 2, 2]