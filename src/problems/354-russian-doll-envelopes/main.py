from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []

        for num in nums:
            if len(lis) == 0 or lis[-1] < num:
                lis.append(num)
            else:
                idx = bisect.bisect_left(lis, num)

                lis[idx] = num                

        return len(lis)

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)

        envs = sorted(envelopes, key = lambda x: (x[0], -x[1]))

        heights = list(map(lambda x: x[1], envs))

        return self.lengthOfLIS(heights)


sol = Solution()


assert sol.maxEnvelopes([[1,15],[7,18],[7,6],[7,100],[2,200],[17,30],[17,45],[3,5],[7,8],[3,6],[3,10],[7,20],[17,3],[17,45]]) == 3
assert sol.maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]) == 4
assert sol.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]) == 3
assert sol.maxEnvelopes([[1,1],[1,1],[1,1]]) == 1