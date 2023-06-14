# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = 100001

        if root is not None:
            if root.left is not None:
                res = min(
                    res, 
                    abs(root.val - root.left.val), 
                    self.getMinimumDifference(root.left)
                )
        
            if root.right is not None:
                res = min(
                    res, 
                    abs(root.val - root.right.val), 
                    self.getMinimumDifference(root.right)
                )

        return res


sol = Solution()

assert sol.getMinimumDifference(
    TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(6)
    )   
) == 1
