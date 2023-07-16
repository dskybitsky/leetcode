class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)

        mapping = {}
        mapped = set()

        s1 = [''] * n

        for i in range(n):
            if s[i] not in mapping:
                if t[i] in mapped:
                    return False
                
                mapping[s[i]] = t[i]
                mapped.add(t[i])

            s1[i] = mapping[s[i]]

        return ''.join(s1) == t

    
sol = Solution()

assert sol.isIsomorphic(s = "badc", t = "baba") is False
assert sol.isIsomorphic(s = "egg", t = "add") is True
assert sol.isIsomorphic(s = "foo", t = "bar") is False
assert sol.isIsomorphic(s = "paper", t = "title") is True