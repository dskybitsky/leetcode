from typing import List
import math

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)

        graph = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                dist = math.sqrt((bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2)

                if bombs[i][2] >= dist:
                    graph[i].add(j)
        
        all_bombs = set(range(n))

        res = 0

        while len(all_bombs):
            b = next(iter(all_bombs))

            to_visit = [b]

            visited = set()

            while len(to_visit):
                b1 = to_visit.pop(0)
                
                all_bombs.discard(b1)

                visited.add(b1)

                for b2 in graph[b1]:
                    if b2 not in visited:
                        to_visit.append(b2)
            
            res = max(res, len(visited))

        return res


sol = Solution()

assert sol.maximumDetonation(bombs = [[2,1,3],[6,1,4]]) == 2
assert sol.maximumDetonation(bombs = [[1,1,5],[10,10,5]]) == 1
assert sol.maximumDetonation(bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]) == 5
