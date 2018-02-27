#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/26
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x.start)
        result = []  # 注意：result=temp=[],result和temp指向同一个list
        start, end = intervals[0].start, intervals[0].end
        for i in range(1, len(intervals)):
            if end >= intervals[i].start:
                end = max(end, intervals[i].end)
            else:
                result.append(Interval(start, end))
                start, end = intervals[i].start, intervals[i].end
        result.append(Interval(start, end))
        return result


class Solution2:
    def merge(self, intervals):
        intervals.sort(key = lambda x:x.start)
        merged = []
        for each in intervals:
            if merged and merged[-1].end >= each.start:
                merged[-1].end = max(merged[-1].end, each.end)
            else:
                merged.append(each)
        return merged


if __name__ == '__main__':
    so = Solution()
    intervals = [Interval(1, 4), Interval(1, 4), Interval(5, 6)]
    result = so.merge(intervals)
    print([[x.start, x.end] for x in result])
