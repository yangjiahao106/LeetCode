from typing import *


class Solution:
    # [1,2,3,0, 2]
    # [0,1,2,2, 3]
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * (len(prices))

        for r in range(1, len(prices)):

            for l in range(r, -1, -1):
                if prices[r] < prices[l]:
                    break
                if l < 2:
                    dp[r] = max(max(dp[r - 1], prices[r] - prices[l]), dp[r])
                else:
                    dp[r] = max(max(dp[r - 1], dp[l - 2] + prices[r] - prices[l]), dp[r])


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 3 for i in range(len(prices))]
        # dp[i][0] 持仓状态
        # dp[i][1] 空仓冷冻期 指第i+1天不能交易
        # dp[i][2] 空仓非冷冻期
        dp[0][0] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])

        return max(dp[-1][1], dp[-1][2])
