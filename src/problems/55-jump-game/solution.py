from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        dp = [0] * n

        dp[0] = nums[0]

        for i in range(1, n):
            if dp[i - 1] < i:
                return False

            dp[i] = max(dp[i - 1], i + nums[i])

        return True


if __name__ == '__main__':
    sol = Solution()

    assert sol.canJump([2, 3, 1, 1, 4]) is True
    assert sol.canJump([3, 2, 1, 0, 4]) is False
