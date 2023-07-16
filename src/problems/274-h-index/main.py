from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        citations.sort()

        res = 0

        for i in range(n):
            cit = citations[i]
            papers = n - i

            res = max(res, min(cit, papers))

        return res


sol = Solution()

assert sol.hIndex([100]) == 1
assert sol.hIndex([3,0,6,1,5]) == 3
assert sol.hIndex([1,3,1]) == 1