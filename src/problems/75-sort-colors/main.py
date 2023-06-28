from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        color_index = [0] * 3

        for num in nums:
            color_index[num] += 1
        
        for i in range(n):
            if color_index[0] > 0:
                nums[i] = 0
                color_index[0] -= 1
            elif color_index[1] > 0:
                nums[i] = 1
                color_index[1] -= 1
            else:
                nums[i] = 2

        return


sol = Solution()

nums = [2,0,2,1,1,0]

sol.sortColors(nums)

assert nums == [0,0,1,1,2,2]