class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        sr = s[::-1]

        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]

        for i in range(n):
            for j in range(n):
                if s[i] == sr[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[n][n]


if __name__ == '__main__':
    sol = Solution()

    assert sol.longestPalindromeSubseq("bbbab") == 4
    assert sol.longestPalindromeSubseq("cbbd") == 2
