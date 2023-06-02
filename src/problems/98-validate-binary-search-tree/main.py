import sys
import os
from typing import Optional

current = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(os.path.dirname(current))
sys.path.append(root)

from utils.tree import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode], less: Optional[int] = None, more: Optional[int] = None) -> bool:
        if root is None:
            return True
        
        if less is not None:
            if (
                root.val >= less 
                or root.left is not None and root.left.val >= less
                or root.right is not None and root.right.val >= less
            ):
                return False
        
        if more is not None:
            if (
                root.val <= more 
                or root.left is not None and root.left.val <= more
                or root.right is not None and root.right.val <= more
            ):
                return False
        
        return (
            self.isValidBST(root.left, less = min(less or root.val, root.val), more = more) 
            and self.isValidBST(root.right, less = less, more = max(more or root.val, root.val))
        )


sol = Solution()

assert sol.isValidBST(
    TreeNode(
        2,
        TreeNode(1),
        TreeNode(3)
    )
) is True

assert sol.isValidBST(
    TreeNode(
        5,
        TreeNode(1),
        TreeNode(
            4,
            TreeNode(3),
            TreeNode(6)
        )
    )
) is False

assert sol.isValidBST(
    TreeNode(
        5,
        TreeNode(4),
        TreeNode(
            6,
            TreeNode(3),
            TreeNode(7)
        )
    )
) is False

assert sol.isValidBST(
    TreeNode(
        120,
        TreeNode(
            70,
            TreeNode(
                50,
                TreeNode(20),
                TreeNode(55)
            ),
            TreeNode(
                100,
                TreeNode(75),
                TreeNode(110)
            )
        ),
        TreeNode(
            140,
            TreeNode(
                130,
                TreeNode(119),
                TreeNode(135)
            ),
            TreeNode(
                160,
                TreeNode(150),
                TreeNode(200)
            )
        )
    )
) is False