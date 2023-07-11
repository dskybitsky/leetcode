from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        if (
            p is None and q is not None
            or p is not None and q is None
            or p is not None and q is not None and p.val != q.val
        ):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


sol = Solution()

assert sol.isSameTree(
    TreeNode(1, TreeNode(2), TreeNode(3)),
    TreeNode(1, TreeNode(2), TreeNode(3)),
) is True

assert sol.isSameTree(
    TreeNode(1, TreeNode(2)),
    TreeNode(1, None, TreeNode(2)),
) is False