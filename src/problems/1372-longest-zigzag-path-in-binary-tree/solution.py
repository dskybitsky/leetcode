from tree_node import TreeNode
from typing import Optional

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], depth = -1) -> int:
            if root is None:
                return depth
            
            leftZz = zigZag(root.left, -1, depth + 1)
            rightZz = zigZag(root.right, 1, depth + 1)

            leftDfs = dfs(root.left)
            rightDfs = dfs(root.right)
            
            return max(leftZz, rightZz, leftDfs, rightDfs)

        def zigZag(root: Optional[TreeNode], dir, depth = -1) -> int:
            if root is None:
                return depth
            
            if dir < 0:
                return zigZag(root.right, 1, depth +1)
            
            return zigZag(root.left, -1, depth + 1)
        
        return dfs(root)
        
    

if __name__ == '__main__':
    sol = Solution()

    root1 = TreeNode(
        1,
        None,
        TreeNode(
            1,
            TreeNode(1),
            TreeNode(
                1,
                TreeNode(
                    1,
                    None,
                    TreeNode(
                        1,
                        None,
                        TreeNode(1)
                    )
                ),
                TreeNode(1),
            ),
        )
    )

    assert sol.longestZigZag(root1) == 3