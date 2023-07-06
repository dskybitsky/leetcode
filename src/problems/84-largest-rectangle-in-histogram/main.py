from typing import List
from functools import cache

class Solution:
    def lesserElements(self, nums: List[int], dir: int) -> List[int]:
        n = len(nums)

        stack = []

        res = [None] * n

        dir_range = range(n, -2, -1) if dir > 0 else range(-1, n + 1)

        for i in dir_range:
            num = nums[i] if i >= 0 and i < n else 0
            
            while len(stack) and num <= (nums[stack[0]] if stack[0] >= 0 and stack[0] < n else 0):
                stack.pop(0)

            if i >= 0 and i < n:
                res[i] = stack[0] if len(stack) else None

            stack.insert(0, i)

        return res
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        res = 0

        prevs = self.lesserElements(heights, -1)
        nexts = self.lesserElements(heights, 1)

        for i in range(n):
            prev = prevs[i] if prevs[i] is not None else i - 1
            next = nexts[i] if nexts[i] is not None else i + 1

            res = max(res, heights[i] * (next - prev - 1))

        return res


sol = Solution()

assert sol.largestRectangleArea([4,2,0,3,2,5]) == 6
assert sol.largestRectangleArea([1,1]) == 2
assert sol.largestRectangleArea([2,1,5,6,2,3]) == 10

print("Ok")