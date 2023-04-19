from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0;
        ans = -10001

        for num in nums:
            sum += num
            ans = max(ans, sum)

            if sum < 0:
                sum = 0

        return ans

if __name__ == '__main__':
    sol = Solution()

    assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23
