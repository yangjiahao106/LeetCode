from typing import *


class Solution:
    """
    状态转移方程

    dp[ i ][ j ] = dp[ i - 1 ][ j - nums[ i ] ] + dp[ i - 1 ][ j + nums[ i ] ]

    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if target > s:
            return 0

        dp = [0] * (s * 2 + 1)
        dp[s] = 1

        # print(dp)
        for n in nums:
            dp2 = [0] * (s * 2 + 1)
            for i in range(len(dp)):
                if dp[i] > 0:
                    dp2[i - n] += dp[i]
                    dp2[i + n] += dp[i]
            dp = dp2
            # print(dp)

        return dp[s + target]


class Solution2:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """寻找需要减去的数字组合 ，转换为0-1 背包问题"""

        s = sum(nums)

        diff = s - target

        if diff < 0 or diff % 2 != 0: # 由于相对于s 最终减去的数量一定是偶数所以 diff 为奇数则无解
            return 0

        neg = diff // 2  # 一个数字加号变为减号，总和缩小了两倍，所以需要除以2 。

        dp = [0] * (neg + 1)
        dp[0] = 1
        for n in nums:
            for i in range(len(dp) - 1, n - 1, -1):
                dp[i] += dp[i - n]

            print(dp)

        return dp[neg]


if __name__ == '__main__':
    print(Solution2().findTargetSumWays([1, 1, 1, 1, 1], 2))
