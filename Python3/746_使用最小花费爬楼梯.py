from typing import *


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost: return 0
        if len(cost) <= 1:
            return cost[0]

        for i in range(2, len(cost)):
            cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]
        return min(cost[-1], cost[-2])


class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)  # 长度加一 存储走完全部梯子的最小消耗

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]
