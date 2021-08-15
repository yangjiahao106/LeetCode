from typing import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 实现一个最小堆
        heap = [0]
        for n in nums:
            if len(heap) <= k:
                heap.append(n)
                l = len(heap) - 1
                while l > 1:
                    if heap[l] < heap[l // 2]:
                        heap[l], heap[l // 2] = heap[l // 2], heap[l]
                    l = l // 2

            elif n > heap[1]:
                heap[1] = n
                i = 1
                while True:
                    maxPos = i
                    if i * 2 < len(heap) and heap[i * 2] < heap[i]:
                        maxPos = i * 2
                    if i * 2 + 1 < len(heap) and heap[i * 2 + 1] < heap[maxPos]:
                        maxPos = i * 2 + 1
                    heap[i], heap[maxPos] = heap[maxPos], heap[i]
                    if i == maxPos:
                        break
                    i = maxPos

        return heap[1]


import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 快速排序思想

        def quick_sort(left, right):
            l, r = left, right
            p = random.randint(left, right)
            nums[l], nums[p] = nums[p], nums[l]
            m = nums[l]

            while l < r:
                while l < r and nums[r] < m:
                    r -= 1
                nums[l], nums[r] = nums[r], nums[l]

                while l < r and nums[l] >= m:
                    l += 1
                nums[l], nums[r] = nums[r], nums[l]

            nums[l] = m

            if l == k - 1:
                return nums[l]

            if l > k - 1:
                return quick_sort(left, l - 1)
            else:
                return quick_sort(l + 1, right)

        return quick_sort(0, len(nums) - 1)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 快速排序思想

        def quick_sort(left, right):
            p = random.randint(left, right)
            nums[right], nums[p] = nums[p], nums[right]
            m = nums[right]

            i = left
            for j in range(left, right):
                if nums[j] > m:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]

            if i == k - 1:
                return nums[i]

            if i > k - 1:
                return quick_sort(left, i - 1)
            else:
                return quick_sort(i + 1, right)

        return quick_sort(0, len(nums) - 1)

if __name__ == '__main__':
    res = Solution().findKthLargest([2, 1], 2)
    print(res)
