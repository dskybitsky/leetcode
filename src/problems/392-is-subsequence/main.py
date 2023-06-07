import bisect


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        th = { }

        for i in range(n):
            if t[i] not in th:
                th[t[i]] = [i]
            else:
                th[t[i]].append(i)

        min_idx = 0

        for i in range(m):
            c = s[i]

            if c not in th:
                return False
            
            pos = bisect.bisect_left(th[c], min_idx)

            if pos == len(th[c]):
                return False
            
            min_idx = th[c][pos] + 1
        
        return True


sol = Solution()

assert sol.isSubsequence(s = "abc", t = "ahbgdc") is True
assert sol.isSubsequence(s = "axc", t = "ahbgdc") is False
