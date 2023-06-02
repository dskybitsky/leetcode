from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        k = k % n

        acc = [0] * k

        for i in range(k):
            acc[i] = nums[n - k + i]

        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]

        for i in range(k):
            nums[i] = acc[i]

        return


sol = Solution()

nums1 = [1,2,3,4,5,6,7]

sol.rotate(nums1, 3)

assert nums1 == [5,6,7,1,2,3,4]