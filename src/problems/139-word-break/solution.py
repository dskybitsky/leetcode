from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordIndex = set(wordDict)

        memo = { }

        def solve(s: str) -> bool:
            if s in memo:
                return memo[s]

            n = len(s)

            if s in wordIndex:
                memo[s] = True
                return True

            for i in range(1, n):
                subs = s[:i]

                if subs in wordIndex and solve(s[i:]):
                    memo[s] = True
                    return True

            memo[s] = False

            return False

        return solve(s)


if __name__ == '__main__':
    sol = Solution()

    assert sol.wordBreak("a", ["b"]) is False
    assert sol.wordBreak("leetcode", ["leet", "code"]) is True
    assert sol.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False