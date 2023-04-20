from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def get_width(indexes: List[int]) -> int:
            return indexes[-1] - indexes[0] + 1
        
        nodes = [root]
        indexes = [1]

        ans = 0

        while len(indexes) > 0:
            ans = max(ans, get_width(indexes))

            next_nodes = []
            next_indexes = []

            for i in range(len(nodes)):
                node = nodes[i]
                
                next_index = indexes[i] * 2

                if node.left is not None:
                    next_nodes.append(node.left)
                    next_indexes.append(next_index - 1)

                if node.right is not None:
                    next_nodes.append(node.right)
                    next_indexes.append(next_index)
            
            nodes = next_nodes.copy()
            indexes = next_indexes.copy()

        return ans


if __name__ == '__main__':
    sol = Solution()

    assert sol.widthOfBinaryTree(
        TreeNode(1)
    ) == 1

    assert sol.widthOfBinaryTree(
        TreeNode(
            1,
            TreeNode(
                3,
                TreeNode(5),
            ),
            TreeNode(2)
        )
    ) == 2

    assert sol.widthOfBinaryTree(
        TreeNode(
            1,
            TreeNode(
                3,
                TreeNode(5),
                TreeNode(3)
            ),
            TreeNode(
                2,
                None,
                TreeNode(9)
            )
        )
    ) == 4

    assert sol.widthOfBinaryTree(
        TreeNode(
            1,
            TreeNode(
                3,
                TreeNode(
                    5,
                    TreeNode(6)
                )
            ),
            TreeNode(
                2,
                None,
                TreeNode(
                    9,
                    TreeNode(7)
                )
            )
        )
    ) == 7
