from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        
        visited = set()
        colors = [0] * n

        next_v = 0

        while next_v < n:
            colors[next_v] = 1
        
            to_visit = [next_v]

            while len(to_visit) > 0:
                v = to_visit.pop(0)
                v_color = colors[v]

                visited.add(v)

                next_v = max(next_v, v)

                for v1 in graph[v]:
                    if v1 in visited:
                        continue

                    if colors[v1] == v_color:
                        return False
                    
                    colors[v1] = -v_color;
            
                    to_visit.append(v1)
            
            next_v += 1
    
        return True
    

sol = Solution()

assert sol.isBipartite([[3], [2, 4], [1], [0, 4], [1, 3]]) is True
assert sol.isBipartite([[4, 1], [0, 2], [1, 3], [2, 4], [3, 0]]) is False
assert sol.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) is False
assert sol.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) is True