from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [1] * n

        mult = 1

        for i in range(1, n):
            mult *= nums[i - 1]
            res[i] = mult

        mult = 1

        for i in range(n - 1, 0, -1):
            mult *= nums[i]
            res[i - 1] *= mult

        return res
    

sol = Solution()

assert sol.productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert sol.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]