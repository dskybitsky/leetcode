class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        stack = []

        for c in s:
            top = stack[len(stack) - 1] if len(stack) > 0 else ''

            if c == ']':
                if top == '[':
                    stack.pop()
                    continue

                return False

            if c == ')':
                if top == '(':
                    stack.pop()
                    continue

                return False

            if c == '}':
                if top == '{':
                    stack.pop()
                    continue

                return False

            stack.append(c)

        return len(stack) == 0


if __name__ == '__main__':
    sol = Solution()

    assert sol.isValid("()")
    assert sol.isValid('()[]{}')
    assert not sol.isValid("(]")
