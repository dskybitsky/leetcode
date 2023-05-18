from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vertices = set(range(n))

        for edge in edges:
            vertices.discard(edge[1])

        return list(vertices)


sol = Solution()


assert sol.findSmallestSetOfVertices(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]) == [0, 3]
assert sol.findSmallestSetOfVertices(5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]) == [0, 2, 3]
