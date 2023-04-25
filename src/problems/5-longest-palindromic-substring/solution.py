class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [0] * n

        dp[0] = 1
        dp[1] = 2 if s[0] == s[1] else 1

        p_len = 2 if s[0] == s[1] else 1
        p_start = 0 if s[0] == s[1] else 1

        for i in range(2, n):
            if s[i] == s[i - dp[i - 1]]:
                dp[i] = dp[i - 1] + 1
            elif s[i] == s[i - dp[i - 1] - 1]:
                dp[i] = dp[i - 1 - 1] + 1
            else:
                dp[i] = 1

            if dp[i] > p_len:
                p_len = dp[i]
                p_start = i - p_len + 1
            
        return s[p_start:p_start + p_len]


if __name__ == '__main__':
    sol = Solution()

    assert sol.longestPalindrome("aba") == "aba"
    assert sol.longestPalindrome("aacabdkacaa") == "aca"
    assert sol.longestPalindrome("babad") == "aba"
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