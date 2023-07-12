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
        
        res = []
        stack = []
        curr = root

        while curr or len(stack):
            while curr:
                stack.insert(0, curr)
                curr = curr.left

            curr = stack.pop(0)

            res.append(curr.val)

            curr = curr.right

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