from functools import cache


class Solution:
    def minimumDeleteSum(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] + ord(word1[j - 1])

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + ord(word2[i - 1])

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        ord(word1[j - 1]) + dp[i][j - 1],
                        ord(word2[i - 1]) + dp[i - 1][j],
                        ord(word1[j - 1]) + ord(word2[i - 1]) + dp[i - 1][j - 1]
                    )

        return dp[n][m]



if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumDeleteSum("sea", "eat") == 231
    assert sol.minimumDeleteSum("delete", "leet") == 403
