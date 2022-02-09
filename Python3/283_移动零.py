from typing import *


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [0,1,0,3,12]
        """

        l = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                l = i
                break
        if l < 0:
            return

        r = l + 1
        while r < len(nums):
            while nums[r] == 0:
                r += 1
            nums[l] = nums[r]
            l += 1
            r += 1

        while l < len(nums):
            nums[l] = 0
            l += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        左指针左边均为非零数；
        右指针左边直到左指针处均为零。
        """

        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
