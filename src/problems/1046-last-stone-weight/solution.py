from typing import List
import heapq
import math


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []

        for stone in stones:
            heapq.heappush(h, (-1) * stone)

        while len(h) > 1:
            s1, s2 = (-1) * heapq.heappop(h), (-1) * heapq.heappop(h)

            s3 = abs(s1 - s2)

            if s3 > 0:
                heapq.heappush(h, (-1) * s3)

        return (-1) * h[0] if len(h) > 0 else 0


if __name__ == '__main__':
    sol = Solution()

    assert sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert sol.lastStoneWeight([1]) == 1