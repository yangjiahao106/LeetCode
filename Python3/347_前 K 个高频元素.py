#! python3
# __author__ = "YangJiaHao"
# date: 2021/5/30

from typing import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n2count = dict()
        for n in nums:
            if n in n2count:
                n2count[n] += 1
            else:
                n2count[n] = 1

        heap = [None]
        for n, c in n2count.items():
            if len(heap) <= k:  # 堆未满
                heap.append((n, c))
                # heapfy
                i = len(heap) - 1
                while i // 2 > 0 and heap[i][1] < heap[i // 2][1]:
                    heap[i], heap[i // 2] = heap[i // 2], heap[i]
                    i = i // 2
            else:
                # 堆满 更新堆顶
                if c > heap[1][1]:
                    heap[1] = (n, c)
                    i = 1
                    p = i
                    while True:
                        if i * 2 < len(heap) and heap[i][1] > heap[i * 2][1]:
                            p = i * 2
                        if i * 2 + 1 < len(heap) and heap[p][1] > heap[i * 2 + 1][1]:
                            p = i * 2 + 1
                        if i == p:
                            break
                        heap[i], heap[p] = heap[p], heap[i]
                        i = p



        res = []
        for i in heap[1:]:
            res.append(i[0])
        print(res)
        return res

if __name__ == '__main__':
    Solution().topKFrequent([6,0,1,4,9,7,-3,1,-4,-8,4,-7,-3,3,2,-3,9,5,-4,0], 6)
