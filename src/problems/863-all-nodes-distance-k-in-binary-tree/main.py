from typing import List

class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj_map = {}

        def buildAdjMap(root: TreeNode) -> None:
            if root.val not in adj_map:
                adj_map[root.val] = set()

            if root.left:
                adj_map[root.val].add(root.left.val)

                if root.left.val not in adj_map:
                    adj_map[root.left.val] = set()

                adj_map[root.left.val].add(root.val)

                buildAdjMap(root.left)

            if root.right:
                adj_map[root.val].add(root.right.val)

                if root.right.val not in adj_map:
                    adj_map[root.right.val] = set()

                adj_map[root.right.val].add(root.val)

                buildAdjMap(root.right)

        result = set()

        visited = set()

        def dfs(val: int, k: int) -> None:
            if k == 0:
                result.add(val)
                return
            
            visited.add(val)
            
            for sib in adj_map[val]:
                if sib not in visited:
                    dfs(sib, k - 1)


        buildAdjMap(root)

        dfs(target, k)

        return list(result)


sol = Solution()

assert sorted(sol.distanceK(
    TreeNode(1),
    1,
    3
)) == sorted([])

assert sorted(sol.distanceK(
    TreeNode(
        3,
        TreeNode(
            5,
            TreeNode(6),
            TreeNode(2, TreeNode(7), TreeNode(4))
        ),
        TreeNode(1, TreeNode(0), TreeNode(8))
    ),
    5,
    2
)) == sorted([7, 4, 1])