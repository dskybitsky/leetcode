from typing import List

class UnionFind:
    def __init__(self, size: int):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, node: int):
        if node == self.root[node]:
            return node
        
        self.root[node] = self.find(self.root[node])
        
        return self.root[node]
        
    def union(self, node1: int, node2: int):
        root1 = self.find(node1)
        root2 = self.find(node2)
        
        if root1 == root2:
            return
        
        if self.rank[root1] > self.rank[root2]:
            self.root[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.root[root1] = root2
        else:
            self.root[root2] = root1
            self.rank[root1] += 1

    def connected(self, node1: int, node2: int):
        return self.find(node1) == self.find(node2)
    

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        
        for edge in edges:
            uf.union(edge[0], edge[1])
        
        return uf.connected(source, destination)
 
   
if __name__ == "__main__":
    sol = Solution()
  
    assert sol.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2) is True
