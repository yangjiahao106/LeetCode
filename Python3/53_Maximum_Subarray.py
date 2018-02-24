#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/24
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(cur_sum, max_sum)
        return max_sum


class Solution2:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [nums[0]]
        for num in nums[1:]:
            dp.append(num + dp[-1] if dp[-1] > 0 else num)
        return max(dp)


if __name__ == '__main__':
    so = Solution2()
    res = so.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(res)
