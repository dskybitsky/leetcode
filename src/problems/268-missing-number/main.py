from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        
        return (1 + n) * n / 2 - s
    
sol = Solution()

assert sol.missingNumber([3,0,1]) == 2