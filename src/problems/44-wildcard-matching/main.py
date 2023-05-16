class Solution:
    def match(self, s, p) -> bool:
        return s == p or p == "?"

    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i - 1][j - 1]
                elif i > 0:
                    dp[i][j] = dp[i - 1][j - 1] and self.match(s[i - 1], p[j - 1])

        return dp[m][n]


sol = Solution()

assert sol.isMatch("adceb", "*a*b") is True
assert sol.isMatch("aa", "a*") is True
assert sol.isMatch("aab", "c*a*b") is False
assert sol.isMatch("aa", "a") is False
assert sol.isMatch("aa", "*") is True
assert sol.isMatch("cb", "?a") is False