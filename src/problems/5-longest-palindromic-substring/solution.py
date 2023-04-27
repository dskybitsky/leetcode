class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        start = 0
        length = 1

        for d in range(n):
            for offset in range(n - d):
                i = offset
                j = d + offset
                if (
                    s[i] == s[j]
                    and (
                        j - i < 2
                        or dp[i + 1][j - 1] == 1
                    )
                ):
                    dp[i][j] = 1

                    if j - i + 1 > length:
                        length = j - i + 1
                        start = i

        return s[start:start + length]
            


if __name__ == '__main__':
    sol = Solution()

    assert sol.longestPalindrome("babad") == "bab"
    assert sol.longestPalindrome("aacabdkacaa") == "aca"
    assert sol.longestPalindrome("aba") == "aba"
    assert sol.longestPalindrome("cbbd") == "bb"


    # babad
    # dabab

    #       b a b a d
    #       0 1 2 3 4
    #       ---------
    # d 0 | 0 0 0 0 1
    # a 1 | 0 1 0 1 0
    # b 2 | 1 0 2 0 0
    # a 3 | 0 1 0 3 0
    # b 4 | 1 0 2 0 0