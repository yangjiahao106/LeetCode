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


if __name__ == '__main__':
    res = Solution().findKthLargest([2, 1], 2)
    print(res)
