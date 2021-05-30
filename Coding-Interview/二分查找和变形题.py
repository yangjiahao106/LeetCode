#! python3
# __author__ = "YangJiaHao"
# date: 2021/3/16
from typing import *


# 查找最后一个值等于给定值的元素
class BinarySearchTheLastOne:
    def __init__(self):
        pass

    @staticmethod
    def solution1(nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = ((high - low) >> 1) + low
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        # 注意 这里只能用high
        if nums[high] == target:
            return high
        return -1

    @staticmethod
    def solution2(nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = ((high - low) >> 1) + low
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                else:
                    low = mid + 1
        return -1


# 查找最后一个小于等于给定值的元素
class BinarySearchLastValueNotBiggerThan:
    @staticmethod
    def solution(nums: List[int], target: int):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = ((high - low) >> 1) + low
            if nums[mid] <= target:
                if mid == len(nums) - 1 or nums[mid + 1] > target:
                    return mid
                low = mid + 1
            else:
                high = mid - 1
        return -1


# 数组是一个循环有序数组，比如 [4，5，6，1，2，3] 实现二分查找
class LeetCode33:
    @staticmethod
    def solution(nums: List[int], target: int):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:  # 当nums[mid]属于左边升序序列时
                if nums[mid] > target and nums[low] <= target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:  # 当nums[mid]属于右边升序序列时
                if nums[mid] < target and nums[high] >= target:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


if __name__ == '__main__':
    res = BinarySearchTheLastOne.solution1([1, 2, 3, 3, 4], 3)
    print(res)
