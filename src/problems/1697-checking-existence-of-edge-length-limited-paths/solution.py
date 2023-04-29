from typing import List

class UnionFind:
    def __init__(self, size: int):
        self.group = [0] * size
        self.rank = [0] * size

        for i in range(size):
            self.group[i] = i

    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])

        return self.group[node]

    def join(self, node1: int, node2: int):
        group1 = self.find(node1)
        group2 = self.find(node2)

        if group1 == group2:
            return
        
        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1

    def are_connected(self, node1: int, node2: int) -> bool:
        return self.find(node1) == self.find(node2)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edge_list: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n_q = len(queries)
        n_e = len(edge_list)

        queries_with_indices = [[] for _ in range(n_q)]

        for i in range(n_q):
            queries_with_indices[i] = [queries[i][0], queries[i][1], queries[i][2], i]

        edge_list.sort(key = lambda x: x[2])

        queries_with_indices.sort(key = lambda x: x[2])

        uf = UnionFind(n)

        ans = [False] * n_q

        e_idx = 0

        for [p, q, limit, orig_idx] in queries_with_indices:
            while e_idx < n_e and edge_list[e_idx][2] < limit:
                node1 = edge_list[e_idx][0]
                node2 = edge_list[e_idx][1]

                uf.join(node1, node2)

                e_idx += 1
            
            ans[orig_idx] = uf.are_connected(p, q)

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