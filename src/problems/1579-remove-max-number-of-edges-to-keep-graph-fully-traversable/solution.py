from typing import List


class UnionFind:
    def __init__(self, size: int):
        self.group = [0] * size
        self.rank = [0] * size
        self.number_of_sets = size

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
        
        self.number_of_sets -= 1

    def are_connected(self, node1: int, node2: int) -> bool:
        return self.find(node1) == self.find(node2)


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        auf = UnionFind(n)
        buf = UnionFind(n)

        skipped_edges = 0

        edges.sort(key = lambda x: -x[0])

        for edge in edges:
            type, node1, node2 = edge[0], edge[1] - 1, edge[2] - 1

            if type == 1:
                if auf.are_connected(node1, node2):
                    skipped_edges += 1
                else:
                    auf.join(node1, node2)
            elif type == 2:
                if buf.are_connected(node1, node2):
                    skipped_edges += 1
                else:
                    buf.join(node1, node2)
            else:
                if auf.are_connected(node1, node2) and buf.are_connected(node1, node2):
                    skipped_edges += 1
                else:
                    auf.join(node1, node2)
                    buf.join(node1, node2)
        
        if auf.number_of_sets > 1 or buf.number_of_sets > 1:
            return -1

        return skipped_edges
    

if __name__ == "__main__":
    sol = Solution()

    assert sol.maxNumEdgesToRemove(4, [[3,1,2],[3,3,4]]) == -1
    assert sol.maxNumEdgesToRemove(2, [[1,1,2],[2,1,2],[3,1,2]]) == 2
    assert sol.maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]) == 2
    assert sol.maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]) == 0
    assert sol.maxNumEdgesToRemove(4, [[3,2,3],[1,1,2],[2,3,4]]) == -1
