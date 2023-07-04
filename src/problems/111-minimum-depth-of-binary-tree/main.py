from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode, d: int = 1) -> int:
            if root.left is None and root.right is None:
                return d
            
            if root.left is not None and root.right is not None:
                return  min(
                    dfs(root.left, d + 1),
                    dfs(root.right, d + 1),
                )

            if root.left is not None:
                return dfs(root.left, d + 1)
            
            return dfs(root.right, d + 1)
        
        if root is None:
            return 0

        return dfs(root)


sol = Solution()

assert sol.minDepth(
    TreeNode(
        3,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7),
        )
    )
)