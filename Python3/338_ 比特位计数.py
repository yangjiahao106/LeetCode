from typing import *


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        i >> 1会把最低位去掉，因此i >> 1 也是比i小的，肯定前面的数组里算过。
        当 i 的最低位是0，则 i 中1的个数和i >> 1中1的个数相同；
        当i的最低位是1，i 中1的个数是 i >> 1中1的个数再加1
        """

        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


