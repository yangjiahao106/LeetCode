class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 0, n
        while l < h:
            m = (h - l) // 2 + l
            if isBadVersion(m):
                h = m
            else:
                l = m + 1
        return l


def isBadVersion():
    pass
