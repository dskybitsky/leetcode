from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        j = n - 1

        while nums[i] > nums[j]:
            mid = i + (j - i) // 2

            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid

        return nums[i]


sol = Solution()

assert sol.findMin([3,4,5,1,2]) == 1
assert sol.findMin([4,5,6,7,0,1,2]) == 0