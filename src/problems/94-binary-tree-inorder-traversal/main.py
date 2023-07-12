from typing import List, Optional
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        h = [(0, root)]

        to_visit = [(0, 100, root)]

        while len(to_visit):
            w, d, node = to_visit.pop(0)

            d1 = d / 2

            if node.left:
                h.append((w - d1, node.left))
                to_visit.append((w - d1, d1, node.left))
            
            if node.right:
                h.append((w + d1, node.right))
                to_visit.append((w + d1, d1, node.right))

        h.sort(key = lambda x: x[0])

        n = len(h)

        res = [0] * n
        
        for i in range(n):
            res[i] = h[i][1].val

        return res


sol = Solution()

assert sol.inorderTraversal(
    TreeNode(
        3,
        TreeNode(
            1,
            None,
            TreeNode(2)
        ),
    )
) == [1, 2, 3]

assert sol.inorderTraversal(
    TreeNode(
        3,
        TreeNode(1),
        TreeNode(2)
    )
) == [1, 3, 2]

assert sol.inorderTraversal(
    TreeNode(
        1,
        None,
        TreeNode(2, TreeNode(3))
    )
) == [1, 3, 2]