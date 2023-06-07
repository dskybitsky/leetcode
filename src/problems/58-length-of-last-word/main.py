class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)

        i = n - 1

        res = 0

        while i >= 0 and s[i] == ' ':
            i -= 1
        
        while i >= 0 and s[i] != ' ':
            i -= 1
            res += 1

        return res