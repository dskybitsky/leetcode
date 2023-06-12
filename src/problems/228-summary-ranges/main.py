from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)

        if n == 0:
            return []

        start = 0
        end = 0

        def toStr(start: int, end: int) -> str:
            return "{0}->{1}".format(nums[start], nums[end]) if start < end else str(nums[start])

        res = []

        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1:
                res.append(toStr(start, end))
                start = i
                end = i
                continue

            end += 1

        res.append(toStr(start, end))

        return res


sol = Solution()

assert sol.summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"]
assert sol.summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]
