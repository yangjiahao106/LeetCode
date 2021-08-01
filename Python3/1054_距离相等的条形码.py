import collections
from typing import *
import heapq


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        i2c = collections.Counter(barcodes)
        heap = []
        for k, c in i2c.items():
            heap.append([-c, k])

        heapq.heapify(heap)
        res = []
        while len(heap) >= 2:
            v1 = heapq.heappop(heap)
            v2 = heapq.heappop(heap)
            res.append(v1[1])
            res.append(v2[1])
            if v1[0] < -1:
                v1[0] += 1
                heapq.heappush(heap, v1)
            if v2[0] < -1:
                v2[0] += 1
                heapq.heappush(heap, v2)
        if heap:
            res.append(heapq.heappop(heap)[1])
        return res


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        data = []
        for i, j in collections.Counter(barcodes).most_common():
            data += [i] * j

        l = len(barcodes)
        ans = [0] * l
        ans[::2] = data[:(l+1)//2]
        ans[1::2] = data[(l+1)//2:]
        return ans
