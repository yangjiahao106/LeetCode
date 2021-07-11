from typing import *


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1: return False
        target = target // 2

        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):

                if j - nums[i - 1] < 0:  # 避免数组越界
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

                if dp[i][target]:
                    return True
        return False


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1: return False
        target = target // 2

        dp = [False] * (target + 1)  # 使用一维 数组
        dp[0] = True

        for i in range(0, len(nums)):

            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] | dp[j - nums[i]]
                if dp[target]:
                    return True
        return False


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """ 牛逼 """
        if sum(nums) & 1 == 0:
            target = sum(nums) >> 1
            cur = {0}
            for i in nums:
                cur |= {i + x for x in cur}
                if target in cur:
                    return True
        return False


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # n = sum(nums)
        # l = len(nums)
        # if n % 2 == 1:
        #     return False
        # target = n // 2
        # dp = [0] * (target + 1)
        # dp[0] = True
        # for num in nums:
        #     for j in range(target, num - 1, -1):
        #         dp[j] = dp[j] | dp[j - num]
        # return dp[-1] == 1
        bitmap, sum_num = 1, 0
        for num in nums:
            bitmap |= bitmap << num
            sum_num += num
        if sum_num & 1 == 1:
            return False
        return (1 << sum_num // 2) & bitmap != 0


if __name__ == '__main__':
    print(Solution().canPartition([1, 2, 5]))
