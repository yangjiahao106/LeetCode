from typing import *


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0] * 3

        for n in nums:
            a = dp[0] + n
            b = dp[1] + n
            c = dp[2] + n

            dp[a % 3] = max(dp[a % 3], a)
            dp[b % 3] = max(dp[b % 3], b)
            dp[c % 3] = max(dp[c % 3], c)
        return dp[0]


if __name__ == '__main__':
    print(Solution().maxSumDivThree([3,6,1,8]))