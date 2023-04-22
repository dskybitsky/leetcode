import functools

class Solution:
    def minInsertions(self, s: str) -> int:
        @functools.lru_cache(maxsize=None)
        def solve(left: int = 0, right: int = len(s) - 1) -> int:
            if left >= right:
                return 0
            
            if s[left] == s[right]:
                return solve(left + 1, right - 1)
            
            return 1 + min(
                solve(left + 1, right),
                solve(left, right - 1)
            )


        return solve()
    

if __name__ == '__main__':
    sol = Solution()

    assert sol.minInsertions("zzazz") == 0
    assert sol.minInsertions("mbadm") == 2
    assert sol.minInsertions("leetcode") == 5