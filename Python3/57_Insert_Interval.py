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
        使用merge_intervals的方法
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)
        merged = []
        for each in intervals:
            if merged and merged[-1].end >= each.start:
                merged[-1].end = max(merged[-1].end, each.end)
            else:
                merged.append(each)
        return merged


class Solution2:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left_intervals, right_intervals = [], []
        start = newInterval.start
        end = newInterval.end
        for each in intervals:
            if each.end < start:
                left_intervals.append(each)
            elif each.start > end:
                right_intervals.append(each)
            else:
                start = min(each.start, start)
                end = max(each.end, end)
        return left_intervals + [Interval(start, end)] + right_intervals


if __name__ == '__main__':
    so = Solution2()
    intervals = [Interval(1, 2), Interval(6, 9), Interval(10, 11)]
    result = so.insert([Interval(1,5)], Interval(2, 3))
    print([[x.start, x.end] for x in result])
