from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        hash = { }

        for num in nums:
            hash[num] = hash[num] + 1 if num in hash else 1

        for num in hash.keys():
            if hash[num] > n / 2:
                return num
            
        return 0


sol = Solution()

assert sol.majorityElement(nums = [3,2,3]) == 3
assert sol.majorityElement(nums = [2,2,1,1,1,2,2]) == 2
