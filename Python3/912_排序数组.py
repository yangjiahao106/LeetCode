from typing import *
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 快排
        def quickSort(left, right):
            if left >= right: return

            pivot = random.randint(left, right)
            nums[right], nums[pivot] = nums[pivot], nums[right]

            l, r = left, right
            m = nums[right]

            while l < r:
                while l < r and nums[l] <= m:
                    l += 1

                nums[r] = nums[l]

                while l < r and nums[r] > m:
                    r -= 1
                nums[l] = nums[r]

            nums[l] = m
            quickSort(left, l - 1)
            quickSort(l + 1, right)

        quickSort(0, len(nums) - 1)
        return nums
