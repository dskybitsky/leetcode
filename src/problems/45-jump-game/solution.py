from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        result = 0

        cur_end, cur_far = 0, 0

        for i in range(n - 1):
            cur_far = max(cur_far, i + nums[i])

            if i == cur_end:
                result += 1
                cur_end = cur_far

        return result

if __name__ == '__main__':
    sol = Solution()

    assert sol.jump([2,1,1,1,1]) == 3
    assert sol.jump([1,1,1,1]) == 3
    assert sol.jump([1,2,3]) == 2
    assert sol.jump([2,3,1,1,4]) == 2
    assert sol.jump([2,3,0,1,4]) == 2
    