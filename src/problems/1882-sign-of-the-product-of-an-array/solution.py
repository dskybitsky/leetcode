from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1

        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign *= -1

        return sign


if __name__ == "__main__":
    sol = Solution()

    assert sol.arraySign([-1,-2,-3,-4,3,2,1]) == 1
    assert sol.arraySign([1,5,0,2,-3]) == 0