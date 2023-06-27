from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        intervals.sort()

        result = [intervals[0]]

        idx_last = 0

        for i in range(1, n):
            last = result[idx_last]

            if intervals[i][0] <= last[1]:
                last[1] = max(intervals[i][1], last[1])
            else:
                result.append(intervals[i])
                idx_last += 1

        return result
    
sol = Solution()

assert sol.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert sol.merge(intervals = [[1,4],[4,5]]) == [[1,5]]
