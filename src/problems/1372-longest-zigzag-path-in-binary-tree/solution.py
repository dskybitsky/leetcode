from tree_node import TreeNode
from typing import Optional

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node: Optional[TreeNode], dir: int, depth = 0) -> int:
            if node is not None:
                self.ans = max(self.ans, depth)

                if dir < 0:
                    dfs(node.left, 1, depth + 1)
                    dfs(node.right, -1, 1)
                else:
                    dfs(node.left, 1, 1)
                    dfs(node.right, -1, depth + 1)

        dfs(root, -1, 0)
        dfs(root, 1, 0)

        return self.ans
    

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