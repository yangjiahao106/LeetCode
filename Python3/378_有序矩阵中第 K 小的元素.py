from typing import *


# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    " 自己实现最小堆 "

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        # 最小队
        def heap_add(heap, v):
            heap.append(v)
            i = len(heap) - 1
            while i > 1 and heap[i // 2][0] > heap[i][0]:
                heap[i], heap[i // 2] = heap[i // 2], heap[i]
                i = i // 2  # 不要漏掉

        def heap_pop(heap):
            v = heap[1]
            heap[1] = heap[-1]
            heap.pop()
            i = 1
            while True:
                maxPos = i
                if i * 2 < len(heap) and heap[i][0] > heap[i * 2][0]: maxPos = i * 2
                if i * 2 + 1 < len(heap) and heap[maxPos][0] > heap[i * 2 + 1][0]: maxPos = i * 2 + 1
                if maxPos == i: break
                heap[i], heap[maxPos] = heap[maxPos], heap[i]
                i = maxPos  # 不要漏了
            return v

        heap = [None]
        for l in matrix:
            heap_add(heap, l)

        for i in range(k - 1):
            l = heap_pop(heap)
            if len(l) > 1:
                heap_add(heap, l[1:])

        return heap_pop(heap)[0]


import heapq


class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)

        ret = 0
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))

        return heapq.heappop(pq)[0]


class Solution3:
    """二分查找"""

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pass