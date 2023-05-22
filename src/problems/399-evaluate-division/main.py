from typing import List, Dict


class Solution:
    def add_edge(self, graph: Dict[str, Dict[str, float]], v1: str, v2: str, val: float):
        if v1 not in graph:
            graph[v1] = { }
        
        graph[v1][v2] = val
        graph[v1][v1] = 1.0
        
        if v2 not in graph:
            graph[v2] = { }
        
        graph[v2][v1] = 1.0 / val
        graph[v2][v2] = 1.0


    def bfs(self, graph: Dict[str, Dict[str, float]], v1: str, v2: str) -> float:
        if v1 not in graph or v2 not in graph:
            return -1.0
        
        if v2 in graph[v1]:
            return graph[v1][v2]

        to_visit = [v1]
        visited = set()

        while len(to_visit) > 0:
            v = to_visit.pop(0)

            visited.add(v)

            if v2 in graph[v]:
                return graph[v1][v] * graph[v][v2]
            
            for v_next in graph[v].keys():
                if v_next not in visited:
                    self.add_edge(graph, v1, v_next, graph[v1][v] * graph[v][v_next])
                    to_visit.append(v_next)
        
        return -1.0
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = { }

        n = len(equations)

        for i in range(n):
            v1, v2 = equations[i]

            self.add_edge(graph, v1, v2, values[i])

        result = []

        for query in queries:
            q1, q2 = query
            
            weight = self.bfs(graph, q1, q2)

            result.append(weight)

        return result


sol = Solution()

assert sol.calcEquation(
    [["a", "b"], ["c", "d"]],
    [1.0, 1.0],
    [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]
) == [-1.00000, -1.00000, 1.00000, 1.00000]

assert sol.calcEquation(
    [["a", "b"], ["b", "c"]],
    [2.0, 3.0],
    [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
) == [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
