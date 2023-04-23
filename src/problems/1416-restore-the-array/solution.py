class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        m = len(s)
        mod = 10 ** 9 + 7

        dp = [0] * (m + 1)

        def dfs(start: int) -> int:
            if dp[start]:
                return dp[start]

            if start == m:
                return 1

            if s[start] == "0":
                return 0

            count = 0

            for end in range(start, m):
                subs = s[start:end + 1]

                if int(subs) > k:
                    break

                count += dfs(end + 1)

            dp[start] = count % mod

            return count

        return dfs(0) % mod


if __name__ == '__main__':
    sol = Solution()

assert sol.numberOfArrays("1317", 2000) == 8
assert sol.numberOfArrays("13171", 20000) == 16
# assert sol.numberOfArrays("1234567890", 90) == 34
# assert sol.numberOfArrays("2020", 30) == 1
# assert sol.numberOfArrays("1000", 10) == 0
# assert sol.numberOfArrays("13171", 1000) == 13
# assert sol.numberOfArrays("131715", 1000) == 26
# assert sol.numberOfArrays("1000", 10000) == 1
