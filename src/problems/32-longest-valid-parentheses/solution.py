class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []

        def stack_last(offset = 1):
            return stack[len(stack) - offset] if len(stack) - offset >= 0 else None

        result = 0

        for c in s:
            top = stack_last()

            if c == ')':
                prevTop = stack_last(2)

                if top == '(' or isinstance(top, int) and prevTop == '(':
                    if isinstance(top, int):
                        stack.pop()
                        stack.pop()
                        size = top
                    else:
                        stack.pop()
                        size = 0

                    size += 2

                    while isinstance(stack_last(), int):
                        size += stack_last()
                        stack.pop()

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
