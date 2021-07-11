from typing import *


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)
        if dp[-1] != float('inf'):
            return dp[-1]
        else:
            return -1
