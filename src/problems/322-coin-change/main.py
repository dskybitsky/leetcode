from typing import List
from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i and dp[i - coin] != -1:
                    if dp[i] == -1:
                        dp[i] = 1 + dp[i - coin]
                    else:
                        dp[i] = min(dp[i], 1 + dp[i - coin])
        
        return dp[amount]

    
sol = Solution()

assert sol.coinChange(coins = [186,419,83,408], amount = 6249) == 20
assert sol.coinChange(coins = [1,2,5], amount = 11) == 3
assert sol.coinChange(coins = [2], amount = 3) == -1
assert sol.coinChange(coins = [1], amount = 0) == 0