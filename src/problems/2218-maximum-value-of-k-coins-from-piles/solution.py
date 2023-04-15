class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        return 0


if __name__ == '__main__':
    sol = Solution()

    assert sol.maxValueOfCoins([[1, 100, 3], [7, 8, 9]], 2) == 101
    assert sol.maxValueOfCoins([
        [100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]
    ]) == 706
