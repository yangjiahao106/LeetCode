from typing import *


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0 or not prices: return 0

        dp = [[0] * 2 for i in range(k)]
        # dp[i][0] 第i次交易持仓时的收益
        # dp[i][1] 第i次交易空仓时的收益

        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[0][0] = max(dp[0][0], 0 - prices[i])  # 第一次买入的最大收益
            dp[0][1] = max(dp[0][1], dp[0][0] + prices[i])  # 第一次卖出的最大收益

            for j in range(1, k):
                dp[j][0] = max(dp[j - 1][0], dp[j - 1][1] - prices[i])
                dp[j][1] = max(dp[j - 1][1], dp[j - 1][0] + prices[i])

        return dp[-1][1]


