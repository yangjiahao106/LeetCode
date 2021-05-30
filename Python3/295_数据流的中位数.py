#! python3
# __author__ = "YangJiaHao"
# date: 2021/5/30
import heapq


class MedianFinder:
    """ 使用两个堆，最大堆存放较小的一般数字， 最小堆存放较大的一半数字"""

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low_heap = []  # 最大堆 （保存负数从而实现最大堆）
        self.high_heap = []  # 最小队

    def addNum(self, num: int) -> None:
        heapq.heappush(self.high_heap, num)
        heapq.heappush(self.low_heap, -heapq.heappop(self.high_heap))

        if len(self.low_heap) > len(self.high_heap):
            heapq.heappush(self.high_heap, -heapq.heappop(self.low_heap))

    def findMedian(self) -> float:

        if len(self.high_heap) == 0: return 0
        if len(self.low_heap) == len(self.high_heap):
            return (self.high_heap[0] - self.low_heap[0]) / 2
        return self.high_heap[0]

    # def addNum(self, num: int) -> None:
    #     if len(self.max_heap) == len(self.min_heap):
    #         heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
    #     else:
    #         heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))
