from typing import *


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp1 = [0] * len(prices)  # 第i天持仓时的最大收益
        dp2 = [0] * len(prices)  # 第i天空仓时的最大收益

        dp1[0] = -prices[0]  # 买入时收益计为负值

        for i in range(1, len(prices)):
            dp1[i] = max(dp1[i - 1], dp2[i - 1] - prices[i])
            dp2[i] = max(dp2[i - 1], dp1[i - 1] + prices[i] - fee)

        return dp2[-1]
