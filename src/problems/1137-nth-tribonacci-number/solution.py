class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * (n + 3)
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

        return dp[n]

if __name__ == '__main__':
    sol = Solution()

    assert sol.tribonacci(0) == 0
    assert sol.tribonacci(1) == 1
    assert sol.tribonacci(2) == 1
    assert sol.tribonacci(3) == 2
    assert sol.tribonacci(4) == 4
    assert sol.tribonacci(25) == 1389537
