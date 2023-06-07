class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(n + 1):
            dp[0][i] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[m][n] == 1


sol = Solution()

assert sol.isSubsequence(s = "abc", t = "ahbgdc") is True
assert sol.isSubsequence(s = "axc", t = "ahbgdc") is False
