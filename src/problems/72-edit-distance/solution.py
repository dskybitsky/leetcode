from functools import cache


class Solution:
    @cache
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0

        m = len(word1)
        n = len(word2)

        if m == 0:
            return n
        
        if n == 0:
            return m

        i = 0

        while i < min(m, n) and word1[i] == word2[i]:
            i += 1
        
        if i == m:
            return n - i

        if i == n:
            return m - i
        
        return 1 + min(
            self.minDistance(word1[i + 1:], word2[i:]),
            self.minDistance(word1[i + 1:], word2[i + 1:]),
            self.minDistance(word1[i:], word2[i + 1:]),
        )


if __name__ == "__main__":
    sol = Solution()

    assert sol.minDistance("park", "spake") == 3
    assert sol.minDistance("sea", "eat") == 2
    assert sol.minDistance("horse", "ros") == 3
    assert sol.minDistance("intention", "execution") == 5
