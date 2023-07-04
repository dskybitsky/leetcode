from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root: Optional[TreeNode], target: int) -> bool:
            if root is None:                
                return False
            
            next_target = target - root.val
            
            if root.left is None and root.right is None and next_target == 0:
                return True

            return dfs(root.left, next_target) or dfs(root.right, next_target)

        return dfs(root, targetSum)


sol = Solution()

assert sol.hasPathSum(
    TreeNode(
        5,
        TreeNode(
            4,
            TreeNode(
                11,
                TreeNode(7),
                TreeNode(2)
            )
        ),
        TreeNode(
            8,
            TreeNode(13),
            TreeNode(
                4,
                TreeNode(5),
                TreeNode(1)
            )
        )
    ),
    22
) is True

assert sol.hasPathSum(
    TreeNode(
        -2,
        None,
        TreeNode(-4)
    ),
    -5
) is False