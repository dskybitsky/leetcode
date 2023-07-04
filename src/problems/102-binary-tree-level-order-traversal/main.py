from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []

        to_visit = [root]

        while len(to_visit):

            level = []
            to_visit_next = []

            while len(to_visit):
                node = to_visit.pop(0)

                level.append(node.val)

                if node.left:
                    to_visit_next.append(node.left)
                
                if node.right:
                    to_visit_next.append(node.right)
            
            to_visit = to_visit_next.copy()
            
            res.append(level)

        return res


sol = Solution()

assert sol.levelOrder(
    TreeNode(
        3,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7)
        )
    )
) == [[3],[9,20],[15,7]]