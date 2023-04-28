class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return 0


if __name__ == "__main__":
    sol = Solution()

    assert sol.minDistance("horse", "ros") == 3
    assert sol.minDistance("intention", "execution") == 5
