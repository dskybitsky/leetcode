from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = nums[0]
        
        for i in range(1, n):
            s ^= nums[i]
        
        return s
    
sol = Solution()

assert sol.singleNumber(nums = [2,2,1]) == 1

print("Ok")
