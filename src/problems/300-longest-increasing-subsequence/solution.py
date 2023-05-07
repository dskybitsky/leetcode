from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        lis = []

        for num in nums:
            if len(lis) == 0 or lis[-1] < num:
                lis.append(num)
            else:
                idx = bisect.bisect_left(lis, num)

                lis[idx] = num                

        return len(lis)


if __name__ == "__main__":
    sol = Solution()

    assert sol.lengthOfLIS([4, 10, 4, 3, 8, 9]) == 3
    assert sol.lengthOfLIS([0]) == 1
    assert sol.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
    assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert sol.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1

    print("OK")