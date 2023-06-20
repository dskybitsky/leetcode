from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        res = [-1] * n

        if 2 * k >= n:
            return res

        rsum = sum(nums[:2 * k + 1])

        for i in range(k, n - k):
            res[i] = rsum // (2 * k + 1)

            if i + k < n - 1:
                rsum -= nums[i - k]
                rsum += nums[i + k + 1]

        return res


    

sol = Solution()

assert sol.getAverages(nums = [7,4,3,9,1,8,5,2,6], k = 3) == [-1,-1,-1,5,4,4,-1,-1,-1]