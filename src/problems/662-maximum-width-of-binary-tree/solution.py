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
            left = -1
            right = -1

            n = len(indexes)

            for i in range(n):
                if indexes[i] == 1:
                    left = i
                    break
            
            if left < 0:
                return 0
            
            for i in range(n - 1, -1, -1):
                if indexes[i] == 1:
                    right = i
                    break
            
            if right == left:
                return 1

            return right - left + 1
        
        nodes = [root]
        indexes = [1]

        has_more_nodes = True

        ans = 0

        while has_more_nodes:
            has_more_nodes = False

            ans = max(ans, get_width(indexes))

            next_nodes = []
            next_indexes = []

            for i in range(len(nodes)):
                if nodes[i] is not None:
                    next_nodes.append(nodes[i].left)
                    next_nodes.append(nodes[i].right)
                    next_indexes.append(1 if nodes[i].left is not None else 0)
                    next_indexes.append(1 if nodes[i].right is not None else 0)
                    has_more_nodes = True
                else:
                    next_nodes.append(None)
                    next_nodes.append(None)
                    next_indexes.append(0)
                    next_indexes.append(0)
            
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
