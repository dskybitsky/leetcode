# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []

        def dfs(root: TreeNode):
            if root.left:
                dfs(root.left)
            
            vals.append(root.val)

            if root.right:
                dfs(root.right)

        dfs(root)

        n = len(vals)

        res = vals[1] - vals[0]

        for i in range(1, n - 1):
            res = min(res, vals[i + 1] - vals[i])
        
        return res


sol = Solution()

assert sol.getMinimumDifference(
    TreeNode(
        0,
        None,
        TreeNode(
            2236,
            TreeNode(
                1277,
                TreeNode(519)
            ),
            TreeNode(2776)
        )
    )   
) == 519

assert sol.getMinimumDifference(
    TreeNode(
        236,
        TreeNode(
            104,
            None,
            TreeNode(227)
        ),
        TreeNode(
            701,
            None,
            TreeNode(911)
        )
    )   
) == 9

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
