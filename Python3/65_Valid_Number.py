#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/1
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except:
            return False