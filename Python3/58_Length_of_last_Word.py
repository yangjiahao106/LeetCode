#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/27

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words[-1]) if words else 0
