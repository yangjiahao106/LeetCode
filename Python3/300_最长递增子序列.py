#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/14
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        time O(n*n)
        """
        if not nums:
            return 0
        dp = [1] * len(nums)  # dp[0] 占位
        res = 1
        for right in range(0, len(nums)):
            for left in range(0, right):
                if nums[right] > nums[left]:
                    dp[right] = max(dp[right], dp[left] + 1)
                    res = max(res, dp[right])

        return res


from typing import *


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [0] * len(nums)  # dp 最终存放长递增子序列，
        res = 0
        for x in nums:
            l, r = 0, res
            while l < r:  # 查找新数字的插入位置，找到位置后将原数字直接覆盖，或者插入到最后面
                m = (l + r) // 2
                if dp[m] < x:
                    l = m + 1
                else:
                    r = m
            dp[l] = x
            res = max(res, l + 1)
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLIS([1, 3, 5, 4, 7]))
