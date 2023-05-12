from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i][0], questions[i][1]

            if i + brainpower > n - 1:
                dp[i] = max(dp[i + 1], points)
            else:
                dp[i] = max(points + dp[i + brainpower + 1], dp[i + 1])

        return dp[0]


sol = Solution()

assert sol.mostPoints([[12,46], [78,19], [63,15], [79,62], [13,10]])
assert sol.mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]) == 5
assert sol.mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 7
