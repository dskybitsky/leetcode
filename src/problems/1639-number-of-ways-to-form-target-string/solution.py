from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(target)
        m = len(words[0])

        def countCharOnPosInWords(c: str, pos: int) -> int:
            res = 0

            for i in range(len(words)):
                if words[i][pos] == c:
                    res += 1

            return res

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(m + 1):
            dp[0][i] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                cnt = countCharOnPosInWords(target[i - 1], j - 1)

                dp[i][j] = dp[i - 1][j - 1] * cnt + dp[i][j - 1]

        return dp[n][m] % 1000000007


if __name__ == '__main__':
    sol = Solution()

    assert sol.numWays(["acca", "bbbb", "caca"], "aba") == 6
    assert sol.numWays(["abba", "baab"], "bab") == 4
