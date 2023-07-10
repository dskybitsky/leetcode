from typing import List, Optional


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        res = []

        dp = set()

        for l in range(n):
            for i in range(n - l):
                j = i + l

                if (
                    l == 0
                    or l == 1 and s[i] == s[j]
                    or l > 1 and s[i] == s[j] and (i + 1, j - 1) in dp
                ):
                    dp.add((i, j))

        def check(cutpoints: int) -> Optional[List]:
            i = 0
            
            parts = []

            for j in range(n - 1):
                if (1 << j) & cutpoints != 0:
                    if (i, j) not in dp:
                        return None

                    parts.append(s[i:(j + 1)])
                    i = j + 1
            
            if (i, n - 1) not in dp:
                return None
            
            parts.append(s[i:])

            return parts

        for cutpoints in range(1 << (n - 1)):
            cres = check(cutpoints)

            if cres is not None:
                res.append(cres)

        return res


sol = Solution()

assert sol.partition("aab") == [["aa","b"], ["a","a","b"]]
assert sol.partition("a") == [["a"]]
