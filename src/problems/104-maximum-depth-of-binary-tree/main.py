from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], depth: int = 0) -> int:
            if root is None:
                return depth

            return max(
                dfs(root.left, depth + 1),
                dfs(root.right, depth + 1)
            )
        
        return dfs(root)


sol = Solution()

assert sol.maxDepth(
    TreeNode(
        3,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7)
        )
    )
) == 3