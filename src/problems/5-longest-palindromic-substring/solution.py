class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        memo = {}

        def is_palindrome(s: str):
            if s not in memo:
                memo[s] = s == s[::-1]
            
            return memo[s]


        ans = ""
        ans_len = 0

        for i in range(n):
            for j in range(i, n):

                curr_len = j - i + 1

                if curr_len > ans_len:
                    s1 = s[i:j + 1]

                    if is_palindrome(s1):
                        ans = s1
                        ans_len = curr_len

        return ans
            


if __name__ == '__main__':
    sol = Solution()

    assert sol.longestPalindrome("aacabdkacaa") == "aca"
    assert sol.longestPalindrome("aba") == "aba"
    assert sol.longestPalindrome("babad") == "bab"
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