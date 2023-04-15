class Solution:
    def fib(self, n: int) -> int:
        dp = [0] * (n + 2)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]

if __name__ == '__main__':
    sol = Solution()

    assert sol.fib(0) == 0
    assert sol.fib(1) == 1
    assert sol.fib(2) == 1
    assert sol.fib(3) == 2
    assert sol.fib(4) == 3
