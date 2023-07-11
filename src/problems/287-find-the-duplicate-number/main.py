from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        


sol = Solution()

assert sol.findDuplicate([3,1,3,4,2]) == 3
assert sol.findDuplicate([1,3,4,2,2]) == 2
assert sol.findDuplicate([2,2,2,2,2]) == 2
