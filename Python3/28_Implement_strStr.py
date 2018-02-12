#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/12
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

class Solution2:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

if __name__ == '__main__':
    so = Solution()
    res = so.strStr("good", "o")
    print(res)