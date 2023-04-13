from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []

        push_i = 0
        pop_i = 0

        while push_i < n or pop_i < n:
            stack_top = None if len(stack) == 0 else stack[-1]

            if pop_i < n and stack_top == popped[pop_i]:
                stack.pop()
                pop_i += 1
                continue

            if push_i < n:
                stack.append(pushed[push_i])
                push_i += 1
                continue

            return False

        return True


if __name__ == '__main__':

    sol = Solution()

    assert sol.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) is True
    assert sol.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) is False
