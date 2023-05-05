class Solution:
    def isVowel(self, c: str):
        return (
            c == 'a'
            or c == 'e'
            or c == 'i'
            or c == 'o'
            or c == 'u'
        )
    
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)

        ans = 0

        for i in range(k):
            if self.isVowel(s[i]):
                ans += 1

        win = ans

        for i in range(k, n):
            if self.isVowel(s[i]):
                win += 1

            if self.isVowel(s[i - k]):
                win -= 1
            
            ans = max(ans, win)

        return ans


if __name__ == "__main__":
    sol = Solution()

    assert sol.maxVowels("abciiidef", 3) == 3
    assert sol.maxVowels("aeiou", 2) == 2