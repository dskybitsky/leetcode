from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        def get_sum(i: int, j: int) -> int:
            return values[i] + values[j] + i - j

        n = len(values)

        ans = 0

        prev_max = values[0]

        for i in range(1, n):
            ans = max(ans, values[i] - i + prev_max)
            prev_max = max(prev_max, values[i] + i)

        return ans


if __name__ == '__main__':
    sol = Solution()

    assert sol.maxScoreSightseeingPair([2, 7, 7, 2, 1, 7, 10, 4, 3, 3]) == 16
    assert sol.maxScoreSightseeingPair([1, 3, 5]) == 7
    assert sol.maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11
    assert sol.maxScoreSightseeingPair([1, 2]) == 2