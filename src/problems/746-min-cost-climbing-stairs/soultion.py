from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 2], dp[i - 1])

        return min(dp[n - 1], dp[n - 2])


if __name__ == '__main__':
    sol = Solution()

    assert sol.minCostClimbingStairs([4, 1]) == 1
    assert sol.minCostClimbingStairs([10, 15, 20]) == 15
    assert sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
