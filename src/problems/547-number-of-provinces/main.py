from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        all = set(range(n))

        res = 0

        while len(all):
            s = next(iter(all))

            to_visit = [s]

            while len(to_visit):
                s1 = to_visit.pop()

                all.discard(s1)

                for s2 in all:
                    if isConnected[s1][s2] == 1:
                        to_visit.append(s2)

            res += 1

        return res


sol = Solution()

assert sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2
assert sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3

print("Ok")