from typing import *


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0 # 保留的个数
        end = -float('inf')
        for interval in intervals:
            if interval[0] >= end:
                end = interval[1]
                count += 1

        return len(intervals) - count


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 1  # 保留的个数
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] >= end:
                end = interval[1]
                count += 1

        return len(intervals) - count
