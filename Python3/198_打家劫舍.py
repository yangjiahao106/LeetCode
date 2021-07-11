from typing import *



class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = nums
        for i in range(2, len(nums)):
            dp[i] += max(dp[:i - 1])

        return max(dp[-1], dp[-2])

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = nums[:]
        for i in range(2, len(nums)):
            dp[i] += max(dp[i-2] + nums[i], dp[i-1])

        return max(dp[-1], dp[-2])
