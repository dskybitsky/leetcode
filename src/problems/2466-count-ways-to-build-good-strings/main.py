class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[zero] += 1
        dp[one] += 1
        
        mod = 10 ** 9 + 7

        for i in range(min(zero, one) + 1, high + 1):
            if i - zero >= 0:
                dp[i] += dp[i - zero]
            
            if i - one >= 0:
                dp[i] += dp[i - one]

        ans = 0

        for i in range(low, high + 1):
            ans += dp[i]

        return ans % mod
    

sol = Solution()

assert sol.countGoodStrings(low = 5, high = 5, zero = 2, one = 4) == 0
assert sol.countGoodStrings(low = 3, high = 3, zero = 1, one = 1) == 8
assert sol.countGoodStrings(low = 2, high = 3, zero = 1, one = 2) == 5