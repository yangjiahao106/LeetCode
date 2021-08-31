#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/18
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, 0, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        self.reverse(nums, i + 1)  # 翻转后面的增序数字，使其构成的数字最小。
                        return

        self.reverse(nums, 0)

    def reverse(self, nums, start):
        end = len(nums) - 1
        while end > start:
            nums[end], nums[start] = nums[start], nums[end]
            end -= 1
            start += 1


from typing import *


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        要获得一个更大的数，需要将右边的大数与左边的小数交换。
        要想增加的幅度尽可能小，需要满足：
            1：左边的小数尽可能的靠右。
            2：右边的大树尽可能的小
            3：交换后让大数后面的数字升序，即最小。

        实际操作：
            从后向前查找第一个相邻升序的元素对 (i,j)，满足 A[i] < A[j]
            A[i] 即为最靠右的小数。
            在 [j,end) 中找出最小的大数
        """

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, -1, i):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i+1:] = reversed(nums[i+1:])
                        return
        nums[:] = reversed(nums)



if __name__ == '__main__':
    so = Solution()
    so.nextPermutation([4, 3, 2, 1])
