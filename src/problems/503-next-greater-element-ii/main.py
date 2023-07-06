from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        stack = []

        res = [0] * n

        for _ in [0, 1]:
            for i in range(n - 1, -1, -1):
                while len(stack) and nums[i] >= nums[stack[0]]:
                    stack.pop(0)

                res[i] = nums[stack[0]] if len(stack) else -1

                stack.insert(0, i)

        return res
    

sol = Solution()

assert sol.nextGreaterElements([3, 8, 4, 1, 2]) == [8, -1, 8, 2, 3]
assert sol.nextGreaterElements([1,2,3,4,5,6,5,4,5,1,2,3]) == [2,3,4,5,6,-1,6,5,6,2,3,4]
assert sol.nextGreaterElements([1,2,3,2,1]) == [2,3,-1,3,2]
assert sol.nextGreaterElements([5,4,3,2,1]) == [-1,5,5,5,5]
assert sol.nextGreaterElements([1,1,1,1,1]) == [-1,-1,-1,-1,-1]
assert sol.nextGreaterElements([1,5,3,6,8]) == [5,6,6,8,-1]
assert sol.nextGreaterElements([1,2,1]) == [2, -1, 2]
assert sol.nextGreaterElements([1,2,3,4,3]) == [2,3,4,-1,4]