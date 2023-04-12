from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n for i in range(n)]

        dp[0] = 0

        for i in range(n):
            for j in range(i + 1, min(i + nums[i] +  1, n)):
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[n - 1]

if __name__ == '__main__':
    sol = Solution()

    assert sol.jump([2,3,1,1,4]) == 2
    assert sol.jump([2,3,0,1,4]) == 2
    