from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        dp = [10001] * n

        dp[0] = 0

        last_offs = 0

        for i in range(n):
            for offs in range(last_offs + 1, i + nums[i] + 1):
                dp[offs] = min(dp[i] + 1, dp[offs])

                last_offs = offs

                if offs == n - 1:
                    return dp[offs]

        return 0


if __name__ == '__main__':
    sol = Solution()

    assert sol.jump([1]) == 0
    assert sol.jump([2, 1, 1, 1, 1]) == 3
    assert sol.jump([1, 1, 1, 1]) == 3
    assert sol.jump([1, 2, 3]) == 2
    assert sol.jump([2, 3, 1, 1, 4]) == 2
    assert sol.jump([2, 3, 0, 1, 4]) == 2
