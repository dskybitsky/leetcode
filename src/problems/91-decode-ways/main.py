class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if s[0] == "0":
            return 0

        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            num = int(s[i - 1])
            prev_num = int(s[i - 2])

            if num == 0:
                if prev_num != 1 and prev_num != 2:
                    return 0
                
                dp[i] = dp[i - 2]
            else:
                if (
                    prev_num == 1 or prev_num == 2 and num < 7
                ):
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]

        return dp[n]

sol = Solution()

assert sol.numDecodings("1123") == 5
assert sol.numDecodings("2101") == 1
assert sol.numDecodings("27") == 1
assert sol.numDecodings("12") == 2
assert sol.numDecodings("226") == 3