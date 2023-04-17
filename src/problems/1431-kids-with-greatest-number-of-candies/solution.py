from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        max_candies = max(candies)

        result = []

        for i in range(n):
            if candies[i] + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result


if __name__ == '__main__':
    sol = Solution()

    assert sol.kidsWithCandies([2, 3, 5, 1, 3], 3) == [True, True, True, False, True]
