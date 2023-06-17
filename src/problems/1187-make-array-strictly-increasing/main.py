from typing import List, Optional
import bisect


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        m = len(arr1)
        n = len(arr2)

        dp = { }

        def dfs(i, prev):
            if i == m:
                return 0
            
            if (i, prev) in dp:
                return dp[(i, prev)]

            cost = float('inf')
            
            if arr1[i] > prev:
                cost = dfs(i + 1, arr1[i])
            
            idx = bisect.bisect_right(arr2, prev)
            
            if idx < n:
                cost = min(cost, 1 + dfs(i + 1, arr2[idx]))

            dp[(i, prev)] = cost
            
            return cost

        res = dfs(0, -1)
        
        return res if res < float('inf') else -1


sol = Solution()

assert sol.makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]) == 1
assert sol.makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [4,3,1]) == 2
assert sol.makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]) == -1
