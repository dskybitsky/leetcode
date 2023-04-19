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

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        non_circ_sum = self.maxSubArray(nums)

        n = len(nums)
        total_sum = 0

        for i in range(n):
            total_sum += nums[i]
            nums[i] = -nums[i]

        circ_sum = total_sum + self.maxSubArray(nums)

        if circ_sum == 0:
            return non_circ_sum

        return max(circ_sum, non_circ_sum)


if __name__ == '__main__':
    sol = Solution()

    assert sol.maxSubarraySumCircular([5, -3, 5]) == 10
    assert sol.maxSubarraySumCircular([1, -2, 3, -2]) == 3
    assert sol.maxSubarraySumCircular([-3, -2, -3]) == -2
