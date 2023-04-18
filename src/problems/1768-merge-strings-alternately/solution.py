class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []

        n1 = len(word1)
        n2 = len(word2)

        i1, i2 = 0, 0

        while i1 < n1 and i2 < n2:
            ans.append(word1[i1] + word2[i2])
            i1 += 1
            i2 += 1

        if i1 < n1:
            ans.append(word1[i1::])

        if i2 < n2:
            ans.append(word2[i2::])

        return "".join(ans)


if __name__ == '__main__':
    sol = Solution()

    assert sol.mergeAlternately("abc", "pqr") == "apbqcr"
    assert sol.mergeAlternately("ab", "pqrs") == "apbqrs"
