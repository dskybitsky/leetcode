class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)

        if len(t) != n:
            return False

        index = [0] * 26

        for i in range(n):
            sidx = ord(s[i]) - ord('a')
            index[sidx] += 1

            tidx = ord(t[i]) - ord('a')
            index[tidx] -= 1

        for i in index:
            if i != 0:
                return False
        
        return True

sol = Solution()

assert sol.isAnagram(s = "anagram", t = "nagaram") is True
assert sol.isAnagram(s = "rat", t = "car") is False
