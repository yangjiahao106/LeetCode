from typing import *


class Heap():
    def __init__(self):
        self.heap = [-1]

    def heap_add(self, v):
        heap = self.heap

        heap.append(v)
        idx = len(heap) - 1

        while idx > 1 and heap[idx] > heap[idx // 2]:
            heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
            idx = idx // 2

    def heap_pop(self) -> int:
        heap = self.heap
        if len(heap) <= 2: return heap.pop()
        v = heap[1]
        heap[1] = heap.pop()
        idx = 1
        while 1:
            next_idx = idx
            if idx * 2 < len(heap) and heap[idx * 2] > heap[idx]:
                next_idx = idx * 2
            if idx * 2 + 1 < len(heap) and heap[idx * 2 + 1] > heap[next_idx]:
                next_idx = idx * 2 + 1
            if idx == next_idx:
                break
            heap[idx], heap[next_idx] = heap[next_idx], heap[idx]
            idx = next_idx
        return v


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        heap = Heap()  # 最大堆
        capital2profit = []
        for i in range(len(capital)):
            capital2profit.append((capital[i], profits[i]))

        capital2profit.sort(reverse=True)

        for i in range(k):
            # 把能做的项目放入堆中，每次取利润最大的项目做
            while capital2profit and capital2profit[-1][0] <= w:
                heap.heap_add(capital2profit.pop()[1])

            if len(heap.heap) > 1:
                w = w + heap.heap_pop()
            else:
                break
        return w


if __name__ == '__main__':
    s = Solution().findMaximizedCapital(2, 0, [1, 2, 3, 1, 4], [0, 1, 2, 3, 4])
    print(s)
