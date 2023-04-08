from solution import Solution, Node
import unittest

class SolutionTest(unittest.TestCase):
    def test_cloneGraph_2(self):
        node1 = Node(1)
        node2 = Node(2)

        node1.neighbors = [node2]
        node2.neighbors = [node1]

        solution = Solution()

        node_clone1 = solution.cloneGraph(node1)

        self.assertEqual(node_clone1.val, 1)
        self.assertEqual(len(node_clone1.neighbors), 1)

        node_clone2 = node_clone1.neighbors[0]

        self.assertEqual(node_clone2.val, 2)
        self.assertEqual(len(node_clone2.neighbors), 1)

        self.assertEqual(node_clone2.neighbors[0], node_clone1)

    def test_cloneGraph_4(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)

        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node3, node1]

        solution = Solution()

        node_clone1 = solution.cloneGraph(node1)

        self.assertEqual(node_clone1.val, 1)
        self.assertEqual(len(node_clone1.neighbors), 2)

        node_clone2 = node_clone1.neighbors[0]

        self.assertEqual(node_clone2.val, 2)
        self.assertEqual(len(node_clone2.neighbors), 2)

        node_clone4 = node_clone1.neighbors[1]

        self.assertEqual(node_clone4.val, 4)
        self.assertEqual(len(node_clone4.neighbors), 2)

        node_clone3 = node_clone2.neighbors[1]

        self.assertEqual(node_clone3.val, 3)
        self.assertEqual(len(node_clone3.neighbors), 2)

if __name__ == '__main__':
    unittest.main()