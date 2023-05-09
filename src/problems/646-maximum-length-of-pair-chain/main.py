from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)

        pairs = sorted(pairs, key = lambda p: p[1])

        ans = 1

        last = pairs[0]

        for i in range(1, n):
            if last[1] < pairs[i][0]:
                last = pairs[i]
                ans += 1

        return ans
    

sol = Solution()

assert sol.findLongestChain([[1, 2], [2, 3], [3, 4]]) == 2
assert sol.findLongestChain([[1, 2], [7, 8], [4, 5]]) == 3

print("OK")