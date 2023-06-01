from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        index = set(nums)

        res = 0

        while len(index):
            num = next(iter(index))

            seq = 1

            index.discard(num)

            prev = num - 1

            while prev in index:
                seq += 1
                index.discard(prev)
                prev -= 1
            
            nxt = num + 1

            while nxt in index:
                seq += 1
                index.discard(nxt)
                nxt += 1

            res = max(res, seq)

        return res


sol = Solution()

assert sol.longestConsecutive([100,4,200,1,3,2]) == 4
assert sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9