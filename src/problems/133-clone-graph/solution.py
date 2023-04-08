class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        if node == None:
            return None

        return self.cloneNode(node, visited)

    def cloneNode(self, node: 'Node', visited: dict[int, 'Node']) -> 'Node':
        clone = Node(node.val)

        visited[clone.val] = clone

        for n in node.neighbors:
            clone.neighbors.append(
                visited[n.val] if n.val in visited else self.cloneNode(n, visited)
            )

        return clone