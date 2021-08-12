from typing import *
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 快速排序
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


class Solution2:
    # 归并排序
    def sortArray(self, nums: List[int]) -> List[int]:
        temp = nums[:]

        def merge(left, mid, right):
            i = left
            j = mid + 1
            idx = left
            while i <= mid and j <= right:
                if nums[i] < nums[j]:
                    temp[idx] = nums[i]
                    i += 1
                else:
                    temp[idx] = nums[j]
                    j += 1
                idx += 1

            while i <= mid:
                temp[idx] = nums[i]
                idx += 1
                i += 1
            while j <= right:
                temp[idx] = nums[j]
                idx += 1
                j += 1

            for i in range(left, right + 1):
                nums[i] = temp[i]

        def merge_sort(left, right):
            if left >= right:
                return
            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            merge(left, mid, right)

        merge_sort(0, len(nums) - 1)
        return nums