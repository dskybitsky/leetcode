from typing import List


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = { }
        
        for v in range(n):
            graph[v] = { v: 0 }

        for edge in edgeList:
            u, v = edge[0], edge[1]

            if u not in graph:
                graph[u] = { }

            if v not in graph:
                graph[v] = { }

            graph[u][v] = min(graph[u][v], edge[2]) if v in graph[u] else edge[2]
            graph[v][u] = graph[u][v]

        def has_route(p: int, q: int, limit: int) -> bool:
            to_visit = [p]
            visited = set()

            while len(to_visit) > 0:
                u = to_visit.pop()
                visited.add(u)

                if q in graph[u] and graph[u][q] < limit:
                    # graph[p][q] = min(graph[p][q], graph[u][q]) if q in graph[p] else graph[u][q]
                    return True
                
                for v in graph[u].keys():
                    # graph[p][v] = min(graph[p][v], graph[u][v]) if v in graph[p] else graph[u][v]

                    if graph[u][v] < limit and v not in visited:
                        to_visit.append(v)

            return False

        ans = list(map(lambda query: has_route(query[0], query[1], query[2]), queries))

        return ans
    

if __name__ == "__main__":
    sol = Solution()

    assert sol.distanceLimitedPathsExist(
        3,
        [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
        [[0, 1, 2], [0, 2, 5]]
    ) == [False, True]

    assert sol.distanceLimitedPathsExist(
        5,
        [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
        [[0, 4, 14], [1, 4, 13]]
    ) == [True, False]

    assert sol.distanceLimitedPathsExist(
        13,
        [[9,1,53],[3,2,66],[12,5,99],[9,7,26],[1,4,78],[11,1,62],[3,10,50],[12,1,71],[12,6,63],[1,10,63],[9,10,88],[9,11,59],[1,4,37],[4,2,63],[0,2,26],[6,12,98],[9,11,99],[4,5,40],[2,8,25],[4,2,35],[8,10,9],[11,9,25],[10,11,11],[7,6,89],[2,4,99],[10,4,63]],
        [[9,7,65],[9,6,1],[4,5,34],[10,8,43],[3,7,76],[4,2,15],[7,6,52],[2,0,50],[7,6,62],[1,0,81],[4,5,35],[0,11,86],[12,5,50],[11,2,2],[9,5,6],[12,0,95],[10,6,9],[9,4,73],[6,10,48],[12,0,91],[9,10,58],[9,8,73],[2,3,44],[7,11,83],[5,3,14],[6,2,33]]
    ) == [True,False,False,True,True,False,False,True,False,True,False,True,False,False,False,True,False,True,False,True,True,True,False,True,False,False]