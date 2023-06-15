from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        max_lvl = 1

        level = [root]

        curr_lvl = 1

        while level:
            next_level = []
            sum = 0

            while level:
                node = level.pop(0)

                sum += node.val

                if node.left is not None:
                    next_level.append(node.left)
                
                if node.right is not None:
                    next_level.append(node.right)
            
            if sum > max_sum:
                max_sum = sum
                max_lvl = curr_lvl
            
            curr_lvl += 1
            
            level = next_level

        return max_lvl
    

sol = Solution()

assert sol.maxLevelSum(
    TreeNode(
        1,
        TreeNode(
            7,
            TreeNode(7),
            TreeNode(-8)
        ),
        TreeNode(0)
    )
) == 2