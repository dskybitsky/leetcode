from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums_dict = Counter(nums)
        nums_dict_keys = list(nums_dict.keys())

        def get_score(num: int) -> int:
            return num * nums_dict[num]

        nums_dict_keys.sort()

        n = len(nums_dict_keys)

        if n == 0:
            return 0

        dp = [0] * n

        dp[0] = get_score(nums_dict_keys[0])

        if n == 1:
            return dp[0]

        if nums_dict_keys[1] - nums_dict_keys[0] == 1:
            dp[1] = max(dp[0], get_score(nums_dict_keys[1]))
        else:
            dp[1] = dp[0] + get_score(nums_dict_keys[1])

        for i in range(2, n):
            score = get_score(nums_dict_keys[i])

            if nums_dict_keys[i] - nums_dict_keys[i - 1] == 1:
                dp[i] = max(score + dp[i - 2], dp[i - 1])
            else:
                dp[i] = max(score + dp[i - 2], score + dp[i - 1])

        return dp[n - 1]


if __name__ == '__main__':
    sol = Solution()

    assert sol.deleteAndEarn([3, 1]) == 4
    assert sol.deleteAndEarn([3, 4, 2]) == 6
    assert sol.deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9
