from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        stack = []

        res = [None] * n
        p = 0

        for num in nums:
            if len(stack) == 0:
                stack.insert(0, num)
                continue

            while len(stack) and num > stack[0]:
                res[p] = num
                p += 1
                stack.pop(0)
                
            stack.insert(0, num)
        
        i = 0

        m = len(stack)

        for s in range(m):
            p1 = n - s - 1

            while i < n and nums[i] <= stack[s]:
                i += 1

            res[p1] = nums[i] if i < n else -1

        return res
    

sol = Solution()

assert sol.nextGreaterElements([1,2,3,2,1]) == [2,3,-1,3,2]
assert sol.nextGreaterElements([5,4,3,2,1]) == [-1,5,5,5,5]
assert sol.nextGreaterElements([1,1,1,1,1]) == [-1,-1,-1,-1,-1]
assert sol.nextGreaterElements([1,5,3,6,8]) == [5,6,6,8,-1]
assert sol.nextGreaterElements([1,2,1]) == [2, -1, 2]
assert sol.nextGreaterElements([1,2,3,4,3]) == [2,3,4,-1,4]