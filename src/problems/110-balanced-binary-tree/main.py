from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root: Optional[TreeNode], d: int = 0) -> int:
            if root is None:
                return d
            
            return max(depth(root.left, d + 1), depth(root.right, d + 1))
        
        def solve(root: Optional[TreeNode]) -> bool:
            if root is None:
                return True
            
            if abs(depth(root.left) - depth(root.right)) > 1:
                return False
            
            return solve(root.left) and solve(root.right)
        
        return solve(root)
    


sol = Solution()

assert sol.isBalanced(
    TreeNode(
        1,
        None,
        TreeNode(
            2,
            None,
            TreeNode(3)
        )
    )
) is False

assert sol.isBalanced(
    TreeNode(
        3,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7),
        )
    )
) is True


assert sol.isBalanced(
    TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(
                3,
                TreeNode(4),
                TreeNode(4),
            ),
            TreeNode(3),
        ),
        TreeNode(2)
    )
) is False