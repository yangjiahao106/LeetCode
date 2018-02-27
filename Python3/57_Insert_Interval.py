#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/27
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]

        """
        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self,intervals):
        intervals.sort(key=lambda x:x.start)
        merged = []
        for each in intervals:
            if merged and merged[-1].end >= each.start:
                merged[-1].end = max(merged[-1].end, each.end)
            else:
                merged.append(each)
        return merged