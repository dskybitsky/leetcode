from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + [root.val] + right


sol = Solution()

assert sol.inorderTraversal(
    TreeNode(
        1,
        None,
        TreeNode(2, TreeNode(3))
    )
) == [1, 3, 2]