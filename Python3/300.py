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
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])

        return res


class Solution2:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        time O(n log n)
        """
        dp = [0] * len(nums)
        res = 0

        for x in nums:
            i, j = 0, res
            while i != j:
                m = (i + j) // 2
                if dp[m] < x:
                    i = m + 1
                else:
                    j = m
            dp[i] = x
            res = max(res, i + 1)

        return res