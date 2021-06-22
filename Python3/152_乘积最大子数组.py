from typing import *


class Solution:
    """
    输入为整数，先用0 将nums 分隔为多个部分，如果这个部分包括0个或偶数个负数则最大乘积为所有数的乘积
    如果这个部分包括奇数个负数则最大乘积需要排除最边上的一个负数之外的所有数字
    例如：
    【2，-1，9，8，-1，9，9】
    最大子数据不包含左侧的负数 为 【9，8，-1，9，9】
    """

    def maxProduct(self, nums: List[int]) -> int:
        l, r = 0, 0
        c = 1

        res = nums[0]
        while r < len(nums):
            if nums[r] == 0:
                while l < r - 1:
                    if nums[l] != 0:
                        c /= nums[l]
                        res = max(res, c)
                    l += 1
                l = r
                c = 1
                res = max(res, 0)
            else:
                c *= nums[r]
                res = max(res, c)
            r += 1

        if c < 0:
            while l < r - 1:
                if nums[l] != 0:
                    c /= nums[l]
                    res = max(res, c)
                l += 1

        return int(res)


class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return

        res = nums[0]

        pre_max = nums[0]
        pre_min = nums[0]

        for num in nums[1:]:
            if num < 0:  # 如果为负数则 最大值与最小值互换
                pre_max, pre_min = pre_min, pre_max
            pre_max = max(pre_max * num, num)
            pre_min = min(pre_min * num, num)

            res = max(pre_max, res)

        return res


class Solution3:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return

        res = nums[0]
        i_max = nums[0]
        i_min = nums[0]

        for num in nums[1:]:
            mx = i_max
            i_max = max(i_max * num, i_min * num, num)
            i_min = min(i_min * num, mx * num, num)
            res = max(i_max, res)

        return res
