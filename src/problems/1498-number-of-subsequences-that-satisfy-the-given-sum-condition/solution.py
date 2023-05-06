from typing import List
from bisect import bisect_right


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)

        nums.sort()

        ans = 0

        for left in range(n):
            right = bisect_right(nums, target - nums[left]) - 1

            if left <= right:
                ans += 2 ** (right - left)

        return ans % 1000000007
    

if __name__ == "__main__":
    sol = Solution()

    assert sol.numSubseq([7, 10, 7, 5, 6, 7, 3, 4, 9, 6], 9) == 18
    assert sol.numSubseq([3, 5, 6, 7], 9) == 4
    assert sol.numSubseq([3, 3, 6, 8], 10) == 6
    assert sol.numSubseq([2, 3, 3, 4, 6, 7], 12) == 61
    
    print("Ok")
