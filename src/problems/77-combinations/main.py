from typing import List
from functools import cache

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        @cache
        def solve(n1: int, n2: int, k: int) -> List[List[int]]:
            if k == 0:
                return []
            
            res = []

            for ni in range(n1, n2 - k + 2):
                next = solve(ni + 1, n2, k - 1)

                if len(next):
                    for sub in next:
                        res.append([ni] + sub)
                else:
                    res.append([ni])
            
            return res

        res = solve(1, n, k)

        return res


sol = Solution()

assert sol.combine(n = 1, k = 1) == [[1]]
assert sorted(sol.combine(n = 4, k = 2)) == sorted([[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])
assert sorted(sol.combine(n = 4, k = 3)) == sorted([[1,2,3],[1,2,4],[1,3,4],[2,3,4]])
