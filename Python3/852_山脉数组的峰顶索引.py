from typing import *


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i = 0
        for i in range(0, len(arr) - 2):
            if arr[i] > arr[i + 1]:
                return i
        return i


class Solution2:
    """
    二分查找，根据单调性来判断是在左侧还是右侧
    """

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r) // 2
            if arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m
        return l
