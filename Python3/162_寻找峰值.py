from typing import *

"""
相关题目 852
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if (m == 0 or nums[m - 1] < nums[m]) and \
                    (m == len(nums) - 1 or nums[m + 1] < nums[m]):
                return m
            if m < len(nums) - 1 and nums[m + 1] > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]: # 由于 l != r 所以 nums[m] 不可能是最后一个元素，nums[m+1] 不可能越界
                l = m + 1  # 由于nums[m] < nums[m + 1] 峰值肯定在后面，所以 l = m + 1，l == r 即可以结束
            else:
                r = m  # nums[m] < nums[m + 1]  时 nums[m] 有可能是峰值 所以 r 不能 = m -1
        return l
