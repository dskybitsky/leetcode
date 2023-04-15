from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)

        def solve(piles: List[List[int]], offsets: List[int], k: int) -> int:
            res = 0

            if k == 0:
                return 0

            if k == 1:
                for i in range(n):
                    if offsets[i] < len(piles[i]):
                        res = max(res, piles[i][offsets[i]])

                return res

            for i in range(n):
                if offsets[i] < len(piles[i]):
                    nextOffsets = offsets.copy()
                    nextOffsets[i] += 1

                    res = max(res, piles[i][offsets[i]] + solve(piles, nextOffsets, k - 1))

            return res

        offsets = [0] * n

        return solve(piles, offsets, k)


if __name__ == '__main__':
    sol = Solution()

    assert sol.maxValueOfCoins(
        [[37, 88], [51, 64, 65, 20, 95, 30, 26], [9, 62, 20], [44]],
        9
    ) == 494

    assert sol.maxValueOfCoins([[1, 100, 3], [7, 8, 9]], 2) == 101
    assert sol.maxValueOfCoins([
        [100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]
    ], 7) == 706
