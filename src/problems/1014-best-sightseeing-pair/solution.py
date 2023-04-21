from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)

        ans = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                ans = max(ans, values[i] + values[j] + i - j)

        return ans


if __name__ == '__main__':
    sol = Solution()

    assert sol.maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11
    assert sol.maxScoreSightseeingPair([1, 2]) == 2