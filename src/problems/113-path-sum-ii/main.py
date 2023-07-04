from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(root: Optional[TreeNode], path: List[int], target: int):
            if root is None:                
                return
            
            next_target = target - root.val
            
            next_path = path.copy()
            
            next_path.append(root.val)

            if root.left is None and root.right is None and next_target == 0:
                res.append(next_path)
                return

            dfs(root.left, next_path, next_target)
            dfs(root.right, next_path, next_target)

        dfs(root, [], targetSum)

        return res


sol = Solution()

assert sol.pathSum(
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
) == [[5,4,11,2],[5,8,4,5]]

assert sol.pathSum(
    TreeNode(
        -2,
        None,
        TreeNode(-3)
    ),
    -5
) == [[-2, -3]]