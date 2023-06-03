from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = [set() for _ in range(n)]

        for i in range(n):
            if manager[i] != -1:
                tree[manager[i]].add(i)
        
        res = 0

        def dfs(root: int) -> int:
            sub_time = 0

            for sub in tree[root]:
                sub_time = max(sub_time, dfs(sub))

            return informTime[root] + sub_time
        
        return dfs(headID)


sol = Solution()

assert sol.numOfMinutes(
    n = 11,
    headID = 4,
    manager = [5,9,6,10,-1,8,9,1,9,3,4],
    informTime = [0,213,0,253,686,170,975,0,261,309,337]
) == 2560

assert sol.numOfMinutes(
    n = 15,
    headID = 0,
    manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6],
    informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
) == 3

assert sol.numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0]) == 0
assert sol.numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]) == 1

print("Ok")