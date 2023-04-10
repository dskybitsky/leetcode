class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return 0

if __name__ == '__main__':
    sol = Solution()

    assert sol.longestValidParentheses("(()") == 2
    assert sol.longestValidParentheses(")()())") == 4
    assert sol.longestValidParentheses("") == 0
