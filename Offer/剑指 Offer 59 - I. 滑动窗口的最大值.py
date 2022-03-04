from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []

        mono_stock = []  # 单调栈 递减

        for i in range(k):
            while mono_stock and nums[i] > mono_stock[-1]:
                mono_stock.pop()
            mono_stock.append(nums[i])

        ans = [mono_stock[0]]

        for i in range(k, len(nums)):

            while mono_stock and nums[i] > mono_stock[-1]:
                mono_stock.pop()

            if mono_stock and nums[i - k] == mono_stock[0]:
                mono_stock = mono_stock[1:]

            mono_stock.append(nums[i])
            ans.append(mono_stock[0])

        return ans


import heapq


class Solution2:
    "优先队列"

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(heap)
        ans = [-heap[0][0]]

        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] < i - k + 1:
                heapq.heappop(heap)
            ans.append(-heap[0][0])

        return ans


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []

        mono_stock = []  # 单调栈 递减 （存下标）

        for i in range(k):
            while mono_stock and nums[i] > nums[mono_stock[-1]]:
                mono_stock.pop()
            mono_stock.append(i)

        ans = [nums[mono_stock[0]]]

        for i in range(k, len(nums)):
            mono_stock.append(i)

            while mono_stock and nums[i] > nums[mono_stock[-1]]:
                mono_stock.pop()

            if mono_stock[0] < i - k + 1:
                mono_stock = mono_stock[1:]

            ans.append(nums[mono_stock[0]])

        return ans
