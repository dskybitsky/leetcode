from solution import Solution, Node
import unittest

class SolutionTest(unittest.TestCase):
    def test_cloneGraph(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)

        node1.neighbors = [node2]
        node2.neighbors = [node3]
        node3.neighbors = [node4]
        node4.neighbors = [node1]

        solution = Solution()

        node_clone1 = solution.cloneGraph(node1)

        self.assertEqual(node_clone1, node1)

if __name__ == '__main__':
    unittest.main()