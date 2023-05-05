class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)
        n = len(s)
    
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for j in range(1, m + 1):
            for i in range(j, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][m]


if __name__ == "__main__":
    sol = Solution()

    assert sol.numDistinct("rabbbit", "rabbit") == 3

#     r a b b i t
#   r 1 0 0 0 0 0
#   a 1 1 0 0 0 0 
#   b 1 1 1 0 0 0
#   b 1 1 2 1 0 0
#   b 1 1 3 3 0 0
#   i 1 1 3 3 3 0
#   t 1 1 3 3 3 3

    assert sol.numDistinct("babgbag", "bag") == 5

# (0, 1); (0, 5); (2, 1); (2, 5); (4, 1); (4, 5);

#     b a g   
#   b 1 0 0
#   a 1 1 0
#   b 2 1 0
#   g 2 1 1
#   b 3 1 1
#   a 3 4 1
#   g 3 4 5
