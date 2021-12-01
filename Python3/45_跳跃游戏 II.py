#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/22
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # 贪婪算法
        """
        if len(nums) <= 1:
            return 0

        jump = step = 0
        pos = 0

        while pos + nums[pos] < len(nums) - 1:
            farthest = 0
            for j in range(1, nums[pos] + 1):
                if (j + nums[pos + j]) > farthest:
                    farthest = j + nums[pos + j]
                    step = j
            pos += step
            jump += 1

        return jump + 1


from typing import *


class Solution:
    """ 差点超时"""

    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0

        for i in range(0, len(nums)):
            for d in range(1, nums[i] + 1):
                if i + d < len(nums):
                    dp[i + d] = min(dp[i + d], dp[i] + 1)

        return dp[-1]


class Solution:
    def jump(self, nums: List[int]) -> int:
        maxPos, end, step = 0, 0, 0
        for i in range(len(nums) - 1):  # 注意：最后一个不需要再处理了
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


if __name__ == '__main__':
    so = Solution()
    res = so.jump([2, 3, 1, 1, 4])
    print(res)
