from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        index = set()

        for num in nums:
            if num in index:
                return True
            
            index.add(num)

        return False

sol = Solution()

assert sol.containsDuplicate([1,2,3,1]) is True