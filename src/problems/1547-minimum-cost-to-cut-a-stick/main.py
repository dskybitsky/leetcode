from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}
        cuts = [0] + sorted(cuts) +[n]

        def cost(left: int, right: int) -> int:
            if (left, right) in memo:
                return memo[(left, right)]

            if right - left == 1:
                return 0

            ans = 10000001

            for mid in range(left + 1, right):
                ans = min(
                    ans,
                    cost(left, mid) + cost(mid, right) + cuts[right] - cuts[left]
                )

            memo[(left, right)] = ans

            return ans

        return cost(0, len(cuts) - 1)


sol = Solution()

assert sol.minCost(n = 7, cuts = [1,3,4,5]) == 16
assert sol.minCost(n = 9, cuts = [5,6,1,4,2]) == 22
