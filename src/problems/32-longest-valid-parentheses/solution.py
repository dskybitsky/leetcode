class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []

        result = 0

        for c in s:
            stack_len = len(stack)

            if c == ')' and stack_len > 0:
                top = stack[-1]

                if top == '(' or isinstance(top, int) and stack_len > 1 and stack[-2] == '(':
                    if isinstance(top, int):
                        stack.pop()
                        stack.pop()
                        size = top
                    else:
                        stack.pop()
                        size = 0

                    size += 2

                    while len(stack) > 0 and isinstance(stack[-1], int):
                        size += stack.pop()

                    result = max(result, size)

                    stack.append(size)

                    continue

            stack.append(c)

        return result

if __name__ == '__main__':
    sol = Solution()

    assert sol.longestValidParentheses("()") == 2
    assert sol.longestValidParentheses(")((()()))((") == 8
    assert sol.longestValidParentheses("(()") == 2
    assert sol.longestValidParentheses(")()())") == 4
    assert sol.longestValidParentheses("") == 0
